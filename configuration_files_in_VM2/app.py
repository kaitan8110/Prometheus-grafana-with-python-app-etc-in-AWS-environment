from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Custom metric - Counter
visit_counter = Counter(
    'page_visits', 'Number of visits to the page', ['endpoint']
)

# Custom metric - Gauge
inventory_gauge = Gauge(
    'inventory', 'Current inventory level', ['item']
)


# Initialize inventory for demonstration
inventory = {
    'item1': 5,
    'item2': 10
}

@app.route('/')
def main():
    visit_counter.labels(endpoint='/').inc()  # Increment counter
    return "Welcome to the Python app with Prometheus metrics!"

@app.route('/visit-item1')
def visit_item1():
    visit_counter.labels(endpoint='/visit-item1').inc()  # Increment counter
    inventory['item1'] -= 1  # Simulate an inventory change
    inventory_gauge.labels(item='item1').set(inventory['item1'])  # Update gauge
    return f"Visited item1. Inventory: {inventory['item1']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
