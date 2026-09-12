from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from killscore import __version__
from killscore.db import db_alive, init_db
from killscore.logging import configure_logging, get_logger
from killscore.settings import settings

log = get_logger("killscore.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    log.info("startup", version=__version__, workers=settings.runner_workers, db=init_db())
    yield
    log.info("shutdown")


app = FastAPI(title="KillScore API", version=__version__, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthz")
def healthz():
    return {
        "status": "ok",
        "version": __version__,
        "db": "up" if db_alive() else "down",
        "runner_workers": settings.runner_workers,
    }
