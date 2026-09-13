import time

from fastapi.testclient import TestClient

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


def _wait_done(client: TestClient, run_id: str, timeout: float = 60) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        body = client.get(f"/v1/runs/{run_id}").json()
        if body["status"] in {"done", "failed"}:
            return body
        time.sleep(0.3)
    raise AssertionError("run did not finish")


def test_inline_run_end_to_end():
    with TestClient(app) as client:
        created = client.post("/v1/runs", json={"inline_source": SOURCE, "inline_tests": TESTS})
        assert created.status_code == 201
        run_id = created.json()["id"]
        body = _wait_done(client, run_id)
        assert body["status"] == "done", body
        assert body["baseline_passed"] == 1
        assert body["total"] >= 2
        survivors = client.get(f"/v1/runs/{run_id}/mutants", params={"status": "survived"}).json()
        assert any(m["description"] == ">= -> >" for m in survivors)
        detail = client.get(f"/v1/mutants/{survivors[0]['id']}").json()
        assert detail["executions"][0]["phase"] == "mutant"


def test_run_requires_input():
    with TestClient(app) as client:
        assert client.post("/v1/runs", json={}).status_code == 422


def test_unknown_preset_400():
    with TestClient(app) as client:
        assert client.post("/v1/runs", json={"repo_preset": "nope"}).status_code == 400


def test_events_snapshot_for_finished_run():
    with TestClient(app) as client:
        run_id = client.post("/v1/runs", json={"inline_source": SOURCE, "inline_tests": TESTS}).json()["id"]
        _wait_done(client, run_id)
        with client.stream("GET", f"/v1/runs/{run_id}/events") as res:
            text = "".join(res.iter_text())
        assert "event: snapshot" in text
        assert "event: done" in text
