import json
import os

LOG_FILE = "data/metrics.json"

# Initialize file
def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

# Save metrics
def log_metrics(query, latency, answer_length):
    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    data.append({
        "query": query,
        "latency": latency,
        "answer_length": answer_length
    })

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Get average latency
def get_avg_latency():
    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    if not data:
        return 0

    return sum(d["latency"] for d in data) / len(data)

# Get average answer length (quality proxy)
def get_avg_length():
    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    if not data:
        return 0

    return sum(d["answer_length"] for d in data) / len(data)