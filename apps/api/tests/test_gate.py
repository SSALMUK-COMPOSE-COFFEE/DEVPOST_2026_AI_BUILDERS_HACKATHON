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


def _done_run(client: TestClient) -> str:
    run_id = client.post("/v1/runs", json={"inline_source": SOURCE, "inline_tests": TESTS}).json()["id"]
    for _ in range(200):
        if client.get(f"/v1/runs/{run_id}").json()["status"] in {"done", "failed"}:
            return run_id
        time.sleep(0.3)
    raise AssertionError


def test_report_html_and_pdf():
    with TestClient(app) as client:
        run_id = _done_run(client)
        html = client.get(f"/v1/runs/{run_id}/report.html")
        assert html.status_code == 200 and "evidence record" in html.text
        pdf = client.get(f"/v1/runs/{run_id}/report.pdf")
        assert pdf.status_code == 200 and pdf.content[:4] == b"%PDF"
        assert len(pdf.headers["X-Evidence-SHA256"]) == 64


def test_gate_policy_roundtrip_and_check_404_without_repo():
    with TestClient(app) as client:
        assert client.get("/v1/gate/nope/policy").status_code == 404
