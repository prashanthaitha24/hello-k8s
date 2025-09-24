import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import re
from app import app  # now import works

def test_root_returns_hello():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Hello, Kubernetes" in resp.get_data(as_text=True)

def test_metrics_endpoint_exposes_prometheus_text():
    client = app.test_client()
    client.get("/")  # increment the counter
    resp = client.get("/metrics")
    text = resp.get_data(as_text=True)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"].startswith("text/plain")
    assert re.search(r"^hello_requests_total\s+\d+", text, re.M)
