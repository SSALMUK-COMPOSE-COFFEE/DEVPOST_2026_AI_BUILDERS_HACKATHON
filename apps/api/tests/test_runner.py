from pathlib import Path

from killscore.runner import discover_targets, run

SRC = '''
def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
'''

TESTS = '''
from mod import clamp

def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10
'''


def _repo(tmp_path: Path) -> Path:
    (tmp_path / "mod.py").write_text(SRC)
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_mod.py").write_text(TESTS)
    (tmp_path / "pyproject.toml").write_text('[tool.pytest.ini_options]\npythonpath = ["."]\n')
    return tmp_path


def test_discover_targets_skips_tests(tmp_path):
    repo = _repo(tmp_path)
    assert [str(p) for p in discover_targets(repo)] == ["mod.py"]


def test_run_reports_verdicts(tmp_path):
    repo = _repo(tmp_path)
    events = []
    result = run(repo, workers=4, timeout=20, on_event=lambda k, d: events.append(k))
    assert result.baseline_passed == 1
    assert result.line_coverage == 1.0
    assert result.total == result.killed + result.survived + result.timeout + result.error
    assert result.killed > 0
    assert result.survived > 0
    assert "done" in events
