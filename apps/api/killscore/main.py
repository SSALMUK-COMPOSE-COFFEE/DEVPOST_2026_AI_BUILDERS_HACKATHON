from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from killscore import __version__
from killscore.db import db_alive, init_db
from killscore.logging import configure_logging, get_logger
from killscore.routes_gate import router as gate_router
from killscore.routes_proposals import router as proposals_router
from killscore.routes_runs import router as runs_router
from killscore.seed import seed, seed_runs
from killscore.settings import settings

log = get_logger("killscore.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    ok = init_db()
    if ok:
        seed()
        seed_runs()
    log.info("startup", version=__version__, workers=settings.runner_workers, db=ok)
    yield
    log.info("shutdown")


app = FastAPI(title="KillScore API", version=__version__, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(runs_router)
app.include_router(proposals_router)
app.include_router(gate_router)


@app.get("/healthz")
def healthz():
    return {
        "status": "ok",
        "version": __version__,
        "db": "up" if db_alive() else "down",
        "runner_workers": settings.runner_workers,
    }
