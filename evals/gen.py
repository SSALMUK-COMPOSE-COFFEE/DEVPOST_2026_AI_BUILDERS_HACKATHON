import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
FIXTURES = ROOT / "fixtures"
OUT = ROOT / "out" / "repos"


def load_bugs() -> list[dict]:
    return yaml.safe_load((FIXTURES / "bugs.yaml").read_text())


def generate() -> list[Path]:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    original = (FIXTURES / "billing.py").read_text()
    repos = []
    for bug in load_bugs():
        if original.count(bug["find"]) != 1:
            raise SystemExit(f"{bug['id']}: find string must occur exactly once (found {original.count(bug['find'])})")
        dest = OUT / bug["id"]
        shutil.copytree(FIXTURES, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache", "bugs.yaml"))
        (dest / "billing.py").write_text(original.replace(bug["find"], bug["replace"]))
        repos.append(dest)
    return repos


if __name__ == "__main__":
    paths = generate()
    print(f"generated {len(paths)} repos under {OUT}")
    sys.exit(0)
