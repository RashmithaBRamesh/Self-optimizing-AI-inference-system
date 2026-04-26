import time
from src.feedback import get_avg_latency, get_avg_length

# Track previous latency (simple global)
last_latency = 0.0

def analyze_query(query):
    length = len(query.split())

    if "compare" in query.lower():
        return "high"
    elif length <= 3:
        return "low"
    else:
        return "medium"


def decide_k(query):
    global last_latency

    complexity = analyze_query(query)
    avg_latency = get_avg_latency()
    avg_length = get_avg_length()

    # Base K
    if complexity == "low":
        k = 2
    elif complexity == "medium":
        k = 4
    else:
        k = 6

    # 🔥 Adapt based on latency
    if avg_latency > 2.0:
        k = max(2, k - 2)

    # 🔥 Adapt based on answer quality
    if avg_length < 50:
        k += 1  # increase context

    return k


def update_latency(latency):
    global last_latency
    last_latency = latency