import time

# Track previous latency (simple global)
last_latency = 0.0

def analyze_query(query):
    length = len(query.split())

    # simple complexity detection
    if "compare" in query.lower() or "difference" in query.lower():
        complexity = "high"
    elif length <= 3:
        complexity = "low"
    else:
        complexity = "medium"

    return complexity


def decide_k(query):
    global last_latency

    complexity = analyze_query(query)

    if complexity == "low":
        k = 2
    elif complexity == "medium":
        k = 4
    else:
        k = 6

    # 🔥 latency-based adjustment
    if last_latency > 2.0:
        k = max(2, k - 2)

    return k


def update_latency(latency):
    global last_latency
    last_latency = latency