import shutil
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import select

from killscore import broker
from killscore.db import SessionLocal
from killscore.engine import normalize
from killscore.logging import get_logger
from killscore.models import Mutant, Repo, Run, TargetFunction, TestExecution
from killscore.runner import run as run_mutation
from killscore.scoper import as_filter, scope
from killscore.settings import settings

log = get_logger("killscore.service")
_pool = ThreadPoolExecutor(max_workers=2)

INLINE_TEST_HEADER = "from mod import *\n\n"


def repo_path(repo: Repo) -> Path:
    return (Path(settings.demo_root) / repo.slug).resolve()


def create_inline_repo(run_id: str, source: str, tests: str) -> Path:
    root = Path(settings.runs_root) / run_id
    if root.exists():
        shutil.rmtree(root)
    (root / "tests").mkdir(parents=True)
    (root / "mod.py").write_text(source)
    body = tests if "import" in tests else INLINE_TEST_HEADER + tests
    (root / "tests" / "test_mod.py").write_text(body)
    (root / "pyproject.toml").write_text('[tool.pytest.ini_options]\npythonpath = ["."]\ntestpaths = ["tests"]\n')
    return root


def create_run(repo_slug: str | None, inline_source: str | None, inline_tests: str | None, diff_only: bool) -> Run:
    with SessionLocal() as db:
        repo = None
        if repo_slug:
            repo = db.scalar(select(Repo).where(Repo.slug == repo_slug))
            if repo is None:
                raise ValueError(f"unknown repo preset: {repo_slug}")
        run = Run(repo_id=repo.id if repo else None, diff_only=diff_only and repo is not None, status="queued")
        db.add(run)
        db.commit()
        db.refresh(run)
        path = repo_path(repo) if repo else create_inline_repo(run.id, inline_source or "", inline_tests or "")
        _pool.submit(_execute, run.id, str(path), run.diff_only)
        return run


def _execute(run_id: str, path: str, diff_only: bool) -> None:
    repo = Path(path)
    started = time.monotonic()
    with SessionLocal() as db:
        run = db.get(Run, run_id)
        run.status = "running"
        db.commit()
    broker.publish(run_id, "status", {"status": "running"})

    only = None
    diff_file = repo / "pr.diff"
    if diff_only and diff_file.exists():
        targets = scope(repo, diff_file.read_text())
        only = as_filter(targets)
        with SessionLocal() as db:
            for t in targets:
                db.add(TargetFunction(run_id=run_id, file=t.file, name=t.name, line_start=t.line_start, line_end=t.line_end))
            db.commit()
        broker.publish(run_id, "targets", {"items": [{"file": t.file, "name": t.name, "line_start": t.line_start, "line_end": t.line_end} for t in targets]})

    key_to_id: dict[str, str] = {}

    def on_event(kind: str, data: dict) -> None:
        if kind == "baseline":
            with SessionLocal() as db:
                r = db.get(Run, run_id)
                r.baseline_passed = data["passed"]
                r.line_coverage = data["line_coverage"]
                db.commit()
            broker.publish(run_id, "baseline", data)
        elif kind == "mutants":
            with SessionLocal() as db:
                sources: dict[str, str] = {}
                for item in data["items"]:
                    if item["file"] not in sources:
                        sources[item["file"]] = normalize((repo / item["file"]).read_text())
                    m = Mutant(
                        run_id=run_id, key=item["id"], file=item["file"], function=item["function"],
                        operator=item["operator"], line=item["line"], description=item["description"],
                        original_source=sources[item["file"]], mutant_source=item["source"], status="pending",
                    )
                    db.add(m)
                    db.flush()
                    key_to_id[item["id"]] = m.id
                r = db.get(Run, run_id)
                r.total = data["total"]
                db.commit()
            broker.publish(run_id, "mutants", {"total": data["total"], "items": [
                {"id": key_to_id[i["id"]], "key": i["id"], "file": i["file"], "function": i["function"], "operator": i["operator"], "line": i["line"], "description": i["description"]}
                for i in data["items"]
            ]})
        elif kind == "mutant":
            mid = key_to_id[data["id"]]
            with SessionLocal() as db:
                m = db.get(Mutant, mid)
                m.status = data["verdict"]
                db.add(TestExecution(mutant_id=mid, phase="mutant", exit_code=data["exit_code"], duration_ms=data["duration_ms"], stdout_tail=data["stdout_tail"]))
                r = db.get(Run, run_id)
                setattr(r, data["verdict"], getattr(r, data["verdict"]) + 1)
                db.commit()
            broker.publish(run_id, "mutant", {"id": mid, "key": data["id"], "verdict": data["verdict"], "duration_ms": data["duration_ms"]})

    try:
        result = run_mutation(repo, only_functions=only, workers=settings.runner_workers, timeout=settings.mutant_timeout_sec, on_event=on_event)
        with SessionLocal() as db:
            r = db.get(Run, run_id)
            r.status = "done"
            r.mutation_score = result.score
            r.duration_ms = int((time.monotonic() - started) * 1000)
            r.finished_at = datetime.now(timezone.utc)
            db.commit()
            summary = run_summary(r)
        broker.publish(run_id, "done", summary)
        log.info("run_done", run_id=run_id, score=result.score, total=result.total, duration_ms=summary["duration_ms"])
    except Exception as exc:
        log.error("run_failed", run_id=run_id, error=str(exc))
        with SessionLocal() as db:
            r = db.get(Run, run_id)
            r.status = "failed"
            r.error_message = str(exc)[:2000]
            r.finished_at = datetime.now(timezone.utc)
            db.commit()
        broker.publish(run_id, "failed", {"error": str(exc)[:500]})


def run_summary(run: Run) -> dict:
    return {
        "id": run.id,
        "repo": run.repo.slug if run.repo else None,
        "status": run.status,
        "diff_only": run.diff_only,
        "baseline_passed": run.baseline_passed,
        "line_coverage": run.line_coverage,
        "mutation_score": run.mutation_score,
        "total": run.total,
        "killed": run.killed,
        "survived": run.survived,
        "timeout": run.timeout,
        "error": run.error,
        "duration_ms": run.duration_ms,
        "cost_usd": run.cost_usd,
        "error_message": run.error_message,
        "created_at": run.created_at.isoformat() if run.created_at else None,
        "finished_at": run.finished_at.isoformat() if run.finished_at else None,
    }


def mutant_summary(m: Mutant) -> dict:
    return {
        "id": m.id,
        "key": m.key,
        "file": m.file,
        "function": m.function,
        "operator": m.operator,
        "line": m.line,
        "description": m.description,
        "status": m.status,
        "cluster": m.cluster,
    }
