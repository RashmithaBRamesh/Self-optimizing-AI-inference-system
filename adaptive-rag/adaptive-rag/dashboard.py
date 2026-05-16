import json
import matplotlib.pyplot as plt

# Load metrics
with open("data/metrics.json", "r") as f:
    data = json.load(f)

latencies = [d["latency"] for d in data]
answer_lengths = [d["answer_length"] for d in data]
k_values = [d["k_used"] for d in data]
cache_hits = sum(1 for d in data if d["cache_hit"])

queries = list(range(1, len(data) + 1))

# 📊 Latency Plot
plt.figure(figsize=(8, 5))
plt.plot(queries, latencies)
plt.xlabel("Query Number")
plt.ylabel("Latency (s)")
plt.title("Latency Trend")
plt.grid(True)
plt.show()

# 📊 Answer Length Plot
plt.figure(figsize=(8, 5))
plt.plot(queries, answer_lengths)
plt.xlabel("Query Number")
plt.ylabel("Answer Length")
plt.title("Answer Quality Proxy")
plt.grid(True)
plt.show()

# 📊 Adaptive K Plot
plt.figure(figsize=(8, 5))
plt.plot(queries, k_values)
plt.xlabel("Query Number")
plt.ylabel("K Used")
plt.title("Adaptive Top-K Usage")
plt.grid(True)
plt.show()

print(f"\nTotal Cache Hits: {cache_hits}")