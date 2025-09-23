from flask import Flask
from promethus_client import Counter, generate_latest
import promethus_client

app = Flask(__name__)
REQUESTS = Counter("hello_requests_total", "Total hello requests")

@app.route("/")
def home():
    REQUESTS.inc()
    return "Hello, Kubernetes 👋"

@app.route("/metrics")
def metrics():
    return generate_latest(prometheus_client.REGISTRY), 200, {"Content-Type":"text/plain; version=0.0.4"}
