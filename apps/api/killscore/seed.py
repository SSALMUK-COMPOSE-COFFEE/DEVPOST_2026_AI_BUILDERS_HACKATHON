from pathlib import Path

from sqlalchemy import select

from killscore.db import SessionLocal, init_db
from killscore.models import GatePolicy, Org, Repo
from killscore.settings import settings

PRESETS = [
    ("billing-api", "Billing tiers, discounts, rounding. 100% line coverage, AI-written suite."),
    ("auth-tokens", "Token issuance and expiry. Lower coverage, better tests."),
    ("oss-small", "A vendored small open-source package. Real code, real suite."),
]


def seed() -> None:
    with SessionLocal() as db:
        org = db.scalar(select(Org).where(Org.name == "demo"))
        if org is None:
            org = Org(name="demo", plan="team")
            db.add(org)
            db.flush()
        for slug, desc in PRESETS:
            path = Path(settings.demo_root) / slug
            if not path.exists():
                continue
            repo = db.scalar(select(Repo).where(Repo.slug == slug))
            if repo is None:
                repo = Repo(org_id=org.id, slug=slug, path=str(path.resolve()), description=desc)
                db.add(repo)
                db.flush()
                db.add(GatePolicy(repo_id=repo.id, min_score=0.6, critical_paths=["billing/", "auth/"]))
        db.commit()


if __name__ == "__main__":
    init_db()
    seed()
