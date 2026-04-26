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

    start_total = time.time()

    # 🔥 Adaptive K
    k = decide_k(query)
    print(f"[Adaptive] Using K = {k}")

    # 🔍 Retrieval timing
    start_retrieval = time.time()
    results = retrieve(query, k)
    context = "\n".join(results)
    end_retrieval = time.time()

    # 🤖 Generation timing
    start_gen = time.time()
    answer = generate_response(query, context)
    end_gen = time.time()

    end_total = time.time()

    retrieval_time = end_retrieval - start_retrieval
    generation_time = end_gen - start_gen
    total_latency = end_total - start_total

    update_latency(total_latency)

    log_metrics(query, total_latency, len(answer))

    print(f"\n[Retrieval Time]: {retrieval_time:.2f}s")
    print(f"[Generation Time]: {generation_time:.2f}s")
    print(f"[Total Latency]: {total_latency:.2f}s")

    print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()