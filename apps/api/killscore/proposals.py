import shutil
import tempfile
from pathlib import Path

from sqlalchemy import select

from killscore.db import SessionLocal
from killscore.llm import LLMError, chat_json
from killscore.logging import get_logger
from killscore.models import LLMCall, Mutant, ProposedTest, Run
from killscore.runner import IGNORE, _pytest
from killscore.service import repo_path
from killscore.settings import settings

log = get_logger("killscore.proposals")

PROPOSED_FILE = "tests/test_killscore_proposed.py"

SYSTEM = """You write one pytest test that distinguishes a correct implementation from a mutated one.
You are given the original Python module, a mutant of it (one deliberate change), and the existing tests.
Write a single test function that PASSES on the original module and FAILS on the mutant.
Rules:
- Import exactly like the existing tests do.
- Do not modify the module under test. Do not mock it.
- Target the boundary the mutation changed. Use concrete inputs and exact expected values derived from the ORIGINAL.
- The test must be self-contained and deterministic.
- Return only JSON matching the schema."""

SCHEMA = {
    "type": "object",
    "properties": {
        "test_name": {"type": "string"},
        "test_code": {"type": "string"},
        "targets_mutant_id": {"type": "string"},
        "rationale": {"type": "string"},
    },
    "required": ["test_name", "test_code", "targets_mutant_id", "rationale"],
    "additionalProperties": False,
}


def _existing_tests(repo: Path) -> str:
    parts = []
    for p in sorted(repo.rglob("test_*.py")):
        if PROPOSED_FILE in str(p):
            continue
        parts.append(f"# {p.relative_to(repo)}\n{p.read_text()[:4000]}")
    return "\n\n".join(parts)[:8000]


def _run_with_test(repo: Path, target: str, module_source: str, test_code: str) -> tuple[int | None, str, int]:
    with tempfile.TemporaryDirectory(prefix="ks-prop-") as tmp:
        work = Path(tmp) / "repo"
        shutil.copytree(repo, work, ignore=IGNORE)
        (work / target).write_text(module_source)
        (work / PROPOSED_FILE).parent.mkdir(exist_ok=True)
        (work / PROPOSED_FILE).write_text(test_code)
        return _pytest(work, settings.mutant_timeout_sec * 2, [PROPOSED_FILE])


def propose_test(mutant_id: str) -> ProposedTest:
    with SessionLocal() as db:
        m = db.get(Mutant, mutant_id)
        if m is None:
            raise ValueError("mutant not found")
        run = db.get(Run, m.run_id)
        repo = repo_path(run.repo) if run.repo else Path(settings.runs_root) / run.id
        mutant_key, file, function, description = m.key, m.file, m.function, m.description
        original, mutated = m.original_source, m.mutant_source
        run_id = run.id

    user = (
        f"MUTANT ID: {mutant_key}\nFILE: {file}\nFUNCTION: {function}\nMUTATION: {description}\n\n"
        f"=== ORIGINAL {file} ===\n{original}\n\n=== MUTANT {file} ===\n{mutated}\n\n"
        f"=== EXISTING TESTS ===\n{_existing_tests(repo)}\n"
    )
    proposal = ProposedTest(mutant_id=mutant_id, source="", verdict="pending")
    call = LLMCall(run_id=run_id, purpose="propose_test", model=settings.openrouter_model)
    try:
        result = chat_json(SYSTEM, user, SCHEMA, "propose_test")
        call.model, call.input_tok, call.output_tok = result.model, result.input_tok, result.output_tok
        call.cost_usd, call.latency_ms = result.cost_usd, result.latency_ms
        content = result.content
        if content.get("targets_mutant_id") != mutant_key:
            proposal.verdict = "rejected"
            proposal.rationale = f"model cited mutant {content.get('targets_mutant_id')!r}, which is not this mutant"
            proposal.source = content.get("test_code", "")
            proposal.test_name = content.get("test_name", "")
        else:
            proposal.test_name = content["test_name"]
            proposal.source = content["test_code"]
            proposal.rationale = content["rationale"]
            o_code, o_out, _ = _run_with_test(repo, file, original, proposal.source)
            m_code, m_out, _ = _run_with_test(repo, file, mutated, proposal.source)
            proposal.original_exit, proposal.mutant_exit = o_code, m_code
            if o_code == 0 and m_code == 1:
                proposal.verdict = "verified_kill"
            elif o_code != 0:
                proposal.verdict = "rejected"
                proposal.rationale = f"proposed test fails on the ORIGINAL (exit {o_code}); it encodes a wrong expectation.\n{o_out[-600:]}"
            else:
                proposal.verdict = "rejected"
                proposal.rationale = f"proposed test passes on both original and mutant (mutant exit {m_code}); it does not kill this mutant."
    except LLMError as exc:
        call.ok = False
        proposal.verdict = "error"
        proposal.rationale = str(exc)

    with SessionLocal() as db:
        db.add(call)
        db.flush()
        proposal.llm_call_id = call.id
        db.add(proposal)
        run = db.get(Run, run_id)
        run.cost_usd = (run.cost_usd or 0.0) + call.cost_usd
        db.commit()
        db.refresh(proposal)
        log.info("proposal", mutant=mutant_key, verdict=proposal.verdict, cost=call.cost_usd, latency_ms=call.latency_ms)
        return proposal


def usage_for_run(run_id: str) -> dict:
    with SessionLocal() as db:
        calls = db.scalars(select(LLMCall).where(LLMCall.run_id == run_id).order_by(LLMCall.created_at)).all()
        return {
            "run_id": run_id,
            "calls": len(calls),
            "input_tok": sum(c.input_tok for c in calls),
            "output_tok": sum(c.output_tok for c in calls),
            "cost_usd": round(sum(c.cost_usd for c in calls), 6),
            "p50_latency_ms": sorted(c.latency_ms for c in calls)[len(calls) // 2] if calls else None,
            "items": [{"purpose": c.purpose, "model": c.model, "input_tok": c.input_tok, "output_tok": c.output_tok, "cost_usd": c.cost_usd, "latency_ms": c.latency_ms, "ok": c.ok} for c in calls],
        }
