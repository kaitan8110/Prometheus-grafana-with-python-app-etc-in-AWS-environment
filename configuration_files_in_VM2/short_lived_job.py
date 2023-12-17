from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

def perform_job():
    # Simulate a job, e.g., processing data, performing a calculation, etc.
    import time
    time.sleep(2)  # Simulate some work
    return 42  # Return some result

def push_metrics(job_result):
    registry = CollectorRegistry()
    g = Gauge('job_result', 'Result of the job', registry=registry)
    g.set(job_result)  # Set to the result of your job

    # Push metrics to the Pushgateway
    push_to_gateway('http://52.220.42.49:9091', job='example_batch_job', registry=registry)

if __name__ == "__main__":
    result = perform_job()
    push_metrics(result)
