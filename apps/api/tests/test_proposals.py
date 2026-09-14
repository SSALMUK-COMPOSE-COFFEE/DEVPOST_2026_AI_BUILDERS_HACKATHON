import time

import pytest
from fastapi.testclient import TestClient

from killscore import proposals
from killscore.llm import LLMResult
from killscore.main import app

SOURCE = '''
def is_adult(age):
    return age >= 18
'''

TESTS = '''
def test_is_adult():
    assert is_adult(30)
    assert not is_adult(5)
'''

GOOD_TEST = "from mod import is_adult\n\ndef test_boundary():\n    assert is_adult(18)\n"
WEAK_TEST = "from mod import is_adult\n\ndef test_weak():\n    assert is_adult(40)\n"
WRONG_TEST = "from mod import is_adult\n\ndef test_wrong():\n    assert not is_adult(18)\n"


def _survivor(client: TestClient) -> dict:
    run_id = client.post("/v1/runs", json={"inline_source": SOURCE, "inline_tests": TESTS}).json()["id"]
    for _ in range(200):
        if client.get(f"/v1/runs/{run_id}").json()["status"] in {"done", "failed"}:
            break
        time.sleep(0.3)
    survivors = client.get(f"/v1/runs/{run_id}/mutants", params={"status": "survived"}).json()
    return next(m for m in survivors if m["description"] == ">= -> >")


def _fake(test_code: str, target: str | None = None):
    def fake_chat(system, user, schema, purpose, max_tokens=0):
        key = target or user.split("MUTANT ID: ")[1].split("\n")[0]
        return LLMResult({"test_name": "t", "test_code": test_code, "targets_mutant_id": key, "rationale": "r"}, "fake", 10, 5, 0.001, 12)
    return fake_chat


@pytest.mark.parametrize("code,expected", [(GOOD_TEST, "verified_kill"), (WEAK_TEST, "rejected"), (WRONG_TEST, "rejected")])
def test_verification_loop(monkeypatch, code, expected):
    monkeypatch.setattr(proposals, "chat_json", _fake(code))
    with TestClient(app) as client:
        m = _survivor(client)
        res = client.post(f"/v1/mutants/{m['id']}/propose-test").json()
        assert res["verdict"] == expected, res
        if expected == "verified_kill":
            assert res["original_exit"] == 0 and res["mutant_exit"] == 1
        detail = client.get(f"/v1/mutants/{m['id']}").json()
        assert detail["proposals"][0]["verdict"] == expected
        usage = client.get(f"/v1/usage/{detail['run']['id']}").json()
        assert usage["calls"] == 1 and usage["cost_usd"] > 0


def test_hallucinated_mutant_id_is_hard_rejected(monkeypatch):
    monkeypatch.setattr(proposals, "chat_json", _fake(GOOD_TEST, target="nope::x:0"))
    with TestClient(app) as client:
        m = _survivor(client)
        res = client.post(f"/v1/mutants/{m['id']}/propose-test").json()
        assert res["verdict"] == "rejected"
        assert res["original_exit"] is None
