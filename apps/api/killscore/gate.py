import hashlib
import json

from sqlalchemy import select
from sqlalchemy.orm import Session

from killscore.models import GatePolicy, Mutant, Repo, Run


def latest_run(db: Session, repo: Repo) -> Run | None:
    return db.scalar(select(Run).where(Run.repo_id == repo.id, Run.status == "done").order_by(Run.finished_at.desc()).limit(1))


def policy_for(db: Session, repo: Repo) -> GatePolicy:
    p = db.scalar(select(GatePolicy).where(GatePolicy.repo_id == repo.id))
    if p is None:
        p = GatePolicy(repo_id=repo.id)
        db.add(p)
        db.commit()
        db.refresh(p)
    return p


def evaluate(db: Session, run: Run, policy: GatePolicy) -> dict:
    survivors = db.scalars(select(Mutant).where(Mutant.run_id == run.id, Mutant.status == "survived")).all()
    in_paths = [m for m in survivors if any(m.file.startswith(p) for p in (policy.critical_paths or []))]
    score = run.mutation_score or 0.0
    reasons = []
    if score < policy.min_score:
        reasons.append(f"mutation score {score:.0%} is below the {policy.min_score:.0%} threshold")
    if len(in_paths) > policy.max_survivors_in_paths:
        reasons.append(f"{len(in_paths)} surviving mutant(s) in critical paths (max {policy.max_survivors_in_paths})")
    passed = not reasons
    return {
        "passed": passed,
        "score": score,
        "min_score": policy.min_score,
        "survivors": len(survivors),
        "survivors_in_critical_paths": len(in_paths),
        "critical_paths": policy.critical_paths or [],
        "reasons": reasons,
        "critical_survivors": [{"id": m.id, "function": m.function, "file": m.file, "line": m.line, "description": m.description} for m in in_paths[:10]],
    }


def github_check(repo: Repo, run: Run, verdict: dict) -> dict:
    lines = [
        f"Mutation score: **{verdict['score']:.0%}** (threshold {verdict['min_score']:.0%})",
        f"Line coverage: {run.line_coverage:.0%}" if run.line_coverage is not None else "Line coverage: n/a",
        f"Mutants: {run.killed} killed, {run.survived} survived, {run.timeout} timeout, {run.error} error",
    ]
    if verdict["critical_survivors"]:
        lines.append("")
        lines.append("Surviving mutants in critical paths:")
        for m in verdict["critical_survivors"]:
            lines.append(f"- `{m['file']}::{m['function']}` line {m['line']}: `{m['description']}`")
    return {
        "name": "KillScore / mutation gate",
        "head_sha": run.base_ref or "",
        "status": "completed",
        "conclusion": "success" if verdict["passed"] else "failure",
        "details_url": f"https://killscore.hajin.xyz/runs/{run.id}",
        "output": {
            "title": "Gate passed" if verdict["passed"] else "Gate failed: " + "; ".join(verdict["reasons"]),
            "summary": f"{repo.slug}: mutation score {verdict['score']:.0%}, {verdict['survivors']} survivors",
            "text": "\n".join(lines),
        },
    }


def evidence_hash(run: Run, verdict: dict, mutants: list[Mutant]) -> str:
    payload = {
        "run_id": run.id,
        "finished_at": run.finished_at.isoformat() if run.finished_at else None,
        "score": run.mutation_score,
        "counts": [run.total, run.killed, run.survived, run.timeout, run.error],
        "verdict": verdict["passed"],
        "mutants": [[m.key, m.status] for m in sorted(mutants, key=lambda x: x.key)],
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
