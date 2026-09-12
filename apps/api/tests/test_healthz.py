from fastapi.testclient import TestClient

from killscore.main import app


def test_healthz_shape():
    with TestClient(app) as client:
        body = client.get("/healthz").json()
    assert body["status"] == "ok"
    assert body["db"] in {"up", "down"}
    assert body["runner_workers"] > 0
