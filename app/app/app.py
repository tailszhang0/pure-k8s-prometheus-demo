from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total request count",
    ["method", "endpoint"]
)

@app.before_request
def before_request():
    REQUEST_COUNT.labels("GET", "/").inc()

@app.route('/')
def hello():
    return 'Hello pure-k8s-prometheus-demo World!'

@app.route('/health')
def health():
    return 'pure-k8s-prometheus-demo OK', 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)