import os
import tempfile

os.environ.setdefault("DATABASE_URL", f"sqlite:///{tempfile.mkdtemp()}/test.db")
os.environ.setdefault("RUNS_ROOT", tempfile.mkdtemp())
os.environ.setdefault("LOG_JSON", "false")
