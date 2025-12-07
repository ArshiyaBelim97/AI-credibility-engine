from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ready():
    resp = client.get("/health/ready")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_text_analyze():
    resp = client.post("/analyze/text", data={"text": "This is a plain human-written sentence for testing."})
    assert resp.status_code == 200
    j = resp.json()
    assert "credibility_score" in j

def test_image_analyze(fake_image_path="backend/tests/sample.jpg"):
    # If sample.jpg exists in tests folder
    try:
        with open(fake_image_path, "rb") as f:
            files = {"file": ("sample.jpg", f, "image/jpeg")}
            resp = client.post("/analyze/image", files=files)
            assert resp.status_code == 200
            j = resp.json()
            assert "credibility_score" in j
    except FileNotFoundError:
        # skip if sample image is not present; test for other endpoints still valuable
        pass
