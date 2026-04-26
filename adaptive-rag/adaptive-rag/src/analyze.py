import json
import numpy as np

with open("data/metrics.json", "r") as f:
    data = json.load(f)

latencies = [d["latency"] for d in data]

p50 = np.percentile(latencies, 50)
p95 = np.percentile(latencies, 95)

print(f"P50 Latency: {p50:.2f}s")
print(f"P95 Latency: {p95:.2f}s")