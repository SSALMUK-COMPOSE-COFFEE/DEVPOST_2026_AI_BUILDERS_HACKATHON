import json
from pathlib import Path

from fastapi import APIRouter, HTTPException

from killscore.settings import settings

router = APIRouter(prefix="/v1", tags=["evals"])


@router.get("/evals")
def get_evals():
    path = Path(settings.evals_results)
    if not path.exists():
        raise HTTPException(404, "eval results not generated yet")
    return json.loads(path.read_text())
