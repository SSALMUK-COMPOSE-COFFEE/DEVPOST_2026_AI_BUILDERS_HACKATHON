from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from killscore.db import get_session
from killscore.gate import evaluate, evidence_hash, github_check, latest_run, policy_for
from killscore.models import EvidenceExport, Mutant, Repo, Run
from killscore.report import render_html, render_pdf
from killscore.service import run_summary

router = APIRouter(prefix="/v1", tags=["gate"])


class PolicyIn(BaseModel):
    min_score: float
    max_survivors_in_paths: int = 0
    critical_paths: list[str] = []


def _repo(db: Session, slug: str) -> Repo:
    repo = db.scalar(select(Repo).where(Repo.slug == slug))
    if repo is None:
        raise HTTPException(404, "repo not found")
    return repo


def _policy_out(p) -> dict:
    return {"min_score": p.min_score, "max_survivors_in_paths": p.max_survivors_in_paths, "critical_paths": p.critical_paths or []}


@router.get("/gate/{slug}/policy")
def get_policy(slug: str, db: Session = Depends(get_session)):
    return _policy_out(policy_for(db, _repo(db, slug)))


@router.put("/gate/{slug}/policy")
def put_policy(slug: str, body: PolicyIn, db: Session = Depends(get_session)):
    p = policy_for(db, _repo(db, slug))
    p.min_score = max(0.0, min(1.0, body.min_score))
    p.max_survivors_in_paths = max(0, body.max_survivors_in_paths)
    p.critical_paths = body.critical_paths
    db.commit()
    return _policy_out(p)


@router.get("/gate/{slug}/check")
def get_check(slug: str, min_score: float | None = None, db: Session = Depends(get_session)):
    repo = _repo(db, slug)
    run = latest_run(db, repo)
    if run is None:
        raise HTTPException(404, "no completed run for this repo")
    policy = policy_for(db, repo)
    if min_score is not None:
        policy.min_score = min_score
        db.expunge(policy)
    verdict = evaluate(db, run, policy)
    return {"run": run_summary(run), "verdict": verdict, "github_check": github_check(repo, run, verdict)}


def _run_bundle(db: Session, run_id: str):
    run = db.scalar(select(Run).options(selectinload(Run.repo)).where(Run.id == run_id))
    if run is None or run.status != "done":
        raise HTTPException(404, "completed run not found")
    mutants = db.scalars(select(Mutant).where(Mutant.run_id == run_id).order_by(Mutant.file, Mutant.line)).all()
    policy = policy_for(db, run.repo) if run.repo else type("P", (), {"min_score": 0.6, "max_survivors_in_paths": 0, "critical_paths": []})()
    verdict = evaluate(db, run, policy)
    verdict["max_survivors"] = policy.max_survivors_in_paths
    sha = evidence_hash(run, verdict, mutants)
    return run, mutants, verdict, sha


@router.get("/runs/{run_id}/report.html")
def report_html(run_id: str, db: Session = Depends(get_session)):
    run, mutants, verdict, sha = _run_bundle(db, run_id)
    return Response(render_html(run.repo, run, verdict, mutants, sha), media_type="text/html")


@router.get("/runs/{run_id}/report.pdf")
def report_pdf(run_id: str, db: Session = Depends(get_session)):
    run, mutants, verdict, sha = _run_bundle(db, run_id)
    db.add(EvidenceExport(run_id=run_id, sha256=sha))
    db.commit()
    pdf = render_pdf(render_html(run.repo, run, verdict, mutants, sha))
    return Response(pdf, media_type="application/pdf", headers={"Content-Disposition": f'attachment; filename="killscore-{run_id}.pdf"', "X-Evidence-SHA256": sha})
