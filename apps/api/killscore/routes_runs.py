import asyncio
import json
import queue

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, model_validator
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from sse_starlette.sse import EventSourceResponse

from killscore import broker
from killscore.db import get_session
from killscore.models import Mutant, Repo, Run, TargetFunction
from killscore.service import create_run, mutant_summary, run_summary

router = APIRouter(prefix="/v1", tags=["runs"])


class RunCreate(BaseModel):
    repo_preset: str | None = None
    inline_source: str | None = None
    inline_tests: str | None = None
    diff_only: bool = True

    @model_validator(mode="after")
    def _one_of(self):
        if not self.repo_preset and not (self.inline_source and self.inline_tests):
            raise ValueError("provide repo_preset or inline_source + inline_tests")
        return self


@router.get("/repos")
def list_repos(db: Session = Depends(get_session)):
    repos = db.scalars(select(Repo).order_by(Repo.created_at)).all()
    return [{"slug": r.slug, "description": r.description, "runs": len(r.runs)} for r in repos]


@router.post("/runs", status_code=201)
def post_run(body: RunCreate):
    try:
        run = create_run(body.repo_preset, body.inline_source, body.inline_tests, body.diff_only)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    return {"id": run.id, "status": run.status}


@router.get("/runs")
def list_runs(limit: int = 20, db: Session = Depends(get_session)):
    runs = db.scalars(select(Run).options(selectinload(Run.repo)).order_by(Run.created_at.desc()).limit(limit)).all()
    return [run_summary(r) for r in runs]


def _get_run(run_id: str, db: Session) -> Run:
    run = db.scalar(select(Run).options(selectinload(Run.repo)).where(Run.id == run_id))
    if run is None:
        raise HTTPException(404, "run not found")
    return run


@router.get("/runs/{run_id}")
def get_run(run_id: str, db: Session = Depends(get_session)):
    run = _get_run(run_id, db)
    targets = db.scalars(select(TargetFunction).where(TargetFunction.run_id == run_id)).all()
    return {**run_summary(run), "targets": [{"file": t.file, "name": t.name, "line_start": t.line_start, "line_end": t.line_end} for t in targets]}


@router.get("/runs/{run_id}/mutants")
def list_mutants(run_id: str, status: str | None = Query(None), db: Session = Depends(get_session)):
    _get_run(run_id, db)
    q = select(Mutant).where(Mutant.run_id == run_id)
    if status:
        q = q.where(Mutant.status == status)
    return [mutant_summary(m) for m in db.scalars(q.order_by(Mutant.file, Mutant.line, Mutant.key)).all()]


@router.get("/runs/{run_id}/events")
async def run_events(run_id: str, replay: bool = False, db: Session = Depends(get_session)):
    run = _get_run(run_id, db)
    mutants = db.scalars(select(Mutant).where(Mutant.run_id == run_id).order_by(Mutant.file, Mutant.line, Mutant.key)).all()
    snapshot = {
        "status": run.status,
        "baseline_passed": run.baseline_passed,
        "line_coverage": run.line_coverage,
        "total": run.total,
        "mutants": [mutant_summary(m) for m in mutants],
    }
    finished = run.status in {"done", "failed"}
    summary = run_summary(run)

    async def gen():
        if replay and finished:
            yield {"event": "snapshot", "data": json.dumps({**snapshot, "status": "running", "mutants": [{**m, "status": "pending"} for m in snapshot["mutants"]]})}
            for m in snapshot["mutants"]:
                await asyncio.sleep(0.12)
                yield {"event": "mutant", "data": json.dumps({"kind": "mutant", "id": m["id"], "key": m["key"], "verdict": m["status"], "duration_ms": 0})}
            yield {"event": "done", "data": json.dumps({"kind": "done", **summary})}
            return
        yield {"event": "snapshot", "data": json.dumps(snapshot)}
        if finished:
            yield {"event": "done", "data": json.dumps({"kind": "done", **summary})}
            return
        q = broker.subscribe(run_id)
        try:
            while True:
                try:
                    kind, payload = await asyncio.to_thread(q.get, True, 15)
                except queue.Empty:
                    yield {"event": "ping", "data": "{}"}
                    continue
                yield {"event": kind, "data": payload}
                if kind in {"done", "failed"}:
                    return
        finally:
            broker.unsubscribe(run_id, q)

    return EventSourceResponse(gen())


@router.get("/mutants/{mutant_id}")
def get_mutant(mutant_id: str, db: Session = Depends(get_session)):
    m = db.scalar(select(Mutant).options(selectinload(Mutant.executions), selectinload(Mutant.proposals)).where(Mutant.id == mutant_id))
    if m is None:
        raise HTTPException(404, "mutant not found")
    run = _get_run(m.run_id, db)
    return {
        **mutant_summary(m),
        "run": run_summary(run),
        "original_source": m.original_source,
        "mutant_source": m.mutant_source,
        "executions": [{"phase": e.phase, "exit_code": e.exit_code, "duration_ms": e.duration_ms, "stdout_tail": e.stdout_tail} for e in m.executions],
        "proposals": [
            {"id": p.id, "test_name": p.test_name, "source": p.source, "rationale": p.rationale, "verdict": p.verdict, "original_exit": p.original_exit, "mutant_exit": p.mutant_exit, "created_at": p.created_at.isoformat()}
            for p in m.proposals
        ],
    }
