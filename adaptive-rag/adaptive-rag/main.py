import time
from src.ingest import load_docs
from src.retrieve import retrieve
from src.generate import generate_response
from src.adaptive import decide_k, update_latency
from src.feedback import init_log, log_metrics

def main():
    init_log()
    docs = load_docs("data/docs.txt")

    query = input("Enter query: ")

    start_time = time.time()

    k = decide_k(query)
    print(f"[Adaptive] Using K = {k}")

    results = retrieve(query, k)
    context = "\n".join(results)

    answer = generate_response(query, context)

    end_time = time.time()
    latency = end_time - start_time

    update_latency(latency)

    # 🔥 Log feedback
    log_metrics(query, latency, len(answer))

    print(f"\n[Latency]: {latency:.2f}s")
    print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()