from flask import Flask
from prometheus_client import Counter, generate_latest
import prometheus_client
import os

app = Flask(__name__)
REQUESTS = Counter("hello_requests_total", "Total hello requests")

@app.route("/")
def home():
    REQUESTS.inc()
    return "Hello, Kubernetes 👋"

@app.route("/metrics")
def metrics():
    return generate_latest(prometheus_client.REGISTRY), 200, {"Content-Type":"text/plain; version=0.0.4"}

@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
