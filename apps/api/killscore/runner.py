import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

from killscore.engine import Mutant, generate

IGNORE = shutil.ignore_patterns(".git", ".venv", "__pycache__", ".pytest_cache", "node_modules", ".coverage")


@dataclass(frozen=True)
class Execution:
    mutant_id: str
    verdict: str
    exit_code: int | None
    duration_ms: int
    stdout_tail: str


@dataclass
class RunResult:
    repo: str
    targets: list[str]
    total: int
    killed: int
    survived: int
    timeout: int
    error: int
    line_coverage: float | None
    baseline_passed: int
    executions: list[Execution] = field(default_factory=list)
    mutants: list[Mutant] = field(default_factory=list)

    @property
    def score(self) -> float:
        denom = self.total - self.error
        return self.killed / denom if denom else 0.0


def _network_prefix() -> list[str]:
    try:
        subprocess.run(["unshare", "-rn", "true"], check=True, capture_output=True, timeout=5)
        return ["unshare", "-rn"]
    except Exception:
        return []


NET_PREFIX = _network_prefix()


def _pytest(cwd: Path, timeout: float, extra: list[str] | None = None) -> tuple[int | None, str, int]:
    cmd = NET_PREFIX + [sys.executable, "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider"] + (extra or [])
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"}
    started = time.monotonic()
    try:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, env=env)
        code, out = proc.returncode, proc.stdout + proc.stderr
    except subprocess.TimeoutExpired as exc:
        code, out = None, (exc.stdout or b"").decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
    return code, out[-2000:], int((time.monotonic() - started) * 1000)


def discover_targets(repo: Path) -> list[Path]:
    out = []
    for p in sorted(repo.rglob("*.py")):
        rel = p.relative_to(repo)
        parts = rel.parts
        if any(x in {"tests", "test", ".venv", "__pycache__"} for x in parts):
            continue
        if rel.name.startswith("test_") or rel.name.endswith("_test.py") or rel.name == "conftest.py":
            continue
        out.append(rel)
    return out


def baseline(repo: Path, timeout: float) -> tuple[int, float | None]:
    with tempfile.TemporaryDirectory(prefix="ks-base-") as tmp:
        work = Path(tmp) / "repo"
        shutil.copytree(repo, work, ignore=IGNORE)
        cmd = [sys.executable, "-m", "coverage", "run", "--branch", "-m", "pytest", "-q", "-p", "no:cacheprovider"]
        proc = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=timeout)
        if proc.returncode != 0:
            raise RuntimeError(f"baseline suite failed:\n{proc.stdout[-2000:]}")
        passed = _count_passed(proc.stdout)
        subprocess.run([sys.executable, "-m", "coverage", "json", "-q", "-o", "cov.json"], cwd=work, capture_output=True)
        cov_path = work / "cov.json"
        cov = None
        if cov_path.exists():
            data = json.loads(cov_path.read_text())
            files = {k: v for k, v in data["files"].items() if not Path(k).name.startswith("test_") and "tests" not in Path(k).parts}
            statements = sum(v["summary"]["num_statements"] for v in files.values())
            covered = sum(v["summary"]["covered_lines"] for v in files.values())
            cov = covered / statements if statements else None
        return passed, cov


def _count_passed(stdout: str) -> int:
    for line in reversed(stdout.splitlines()):
        if "passed" in line:
            for tok in line.replace("=", " ").split():
                if tok.isdigit():
                    return int(tok)
    return 0


def execute_one(repo: Path, target: Path, mutant: Mutant, timeout: float) -> Execution:
    with tempfile.TemporaryDirectory(prefix="ks-mut-") as tmp:
        work = Path(tmp) / "repo"
        shutil.copytree(repo, work, ignore=IGNORE)
        (work / target).write_text(mutant.source)
        code, out, ms = _pytest(work, timeout)
    if code is None:
        verdict = "timeout"
    elif code == 0:
        verdict = "survived"
    elif code in (1,):
        verdict = "killed"
    else:
        verdict = "error"
    return Execution(mutant.id, verdict, code, ms, out)


def run(
    repo: Path,
    only_functions: dict[str, set[str]] | None = None,
    workers: int = 8,
    timeout: float = 8.0,
    on_event: Callable[[str, dict], None] | None = None,
) -> RunResult:
    repo = repo.resolve()
    emit = on_event or (lambda *_: None)
    targets = discover_targets(repo)
    if only_functions is not None:
        targets = [t for t in targets if str(t) in only_functions]
    passed, cov = baseline(repo, timeout * 10)
    emit("baseline", {"passed": passed, "line_coverage": cov})

    jobs: list[tuple[Path, Mutant]] = []
    for target in targets:
        funcs = only_functions.get(str(target)) if only_functions else None
        for m in generate((repo / target).read_text(), funcs):
            mid = f"{target}::{m.id}"
            jobs.append((target, Mutant(mid, m.function, m.operator, m.line, m.col, m.description, m.source)))
    emit("mutants", {"total": len(jobs)})

    result = RunResult(str(repo), [str(t) for t in targets], len(jobs), 0, 0, 0, 0, cov, passed, mutants=[m for _, m in jobs])
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(execute_one, repo, t, m, timeout): m for t, m in jobs}
        for fut in as_completed(futures):
            ex = fut.result()
            result.executions.append(ex)
            setattr(result, ex.verdict, getattr(result, ex.verdict) + 1)
            emit("mutant", {"id": ex.mutant_id, "verdict": ex.verdict, "duration_ms": ex.duration_ms})
    emit("done", {"score": result.score, "killed": result.killed, "survived": result.survived, "timeout": result.timeout, "error": result.error})
    return result
