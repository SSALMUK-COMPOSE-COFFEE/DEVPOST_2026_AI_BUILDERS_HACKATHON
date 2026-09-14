from fastapi import APIRouter, HTTPException
from starlette.concurrency import run_in_threadpool

from killscore.proposals import propose_test, usage_for_run

router = APIRouter(prefix="/v1", tags=["proposals"])


def _serialize(p) -> dict:
    return {
        "id": p.id,
        "mutant_id": p.mutant_id,
        "test_name": p.test_name,
        "source": p.source,
        "rationale": p.rationale,
        "verdict": p.verdict,
        "original_exit": p.original_exit,
        "mutant_exit": p.mutant_exit,
        "created_at": p.created_at.isoformat(),
    }


@router.post("/mutants/{mutant_id}/propose-test")
async def post_propose(mutant_id: str):
    try:
        p = await run_in_threadpool(propose_test, mutant_id)
    except ValueError as exc:
        raise HTTPException(404, str(exc))
    return _serialize(p)


@router.get("/usage/{run_id}")
def get_usage(run_id: str):
    return usage_for_run(run_id)
