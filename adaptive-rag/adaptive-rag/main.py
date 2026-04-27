import time
from src.ingest import load_docs
from src.retrieve import retrieve
from src.generate import generate_response
from src.adaptive import decide_k, update_latency
from src.feedback import init_log, log_metrics
from src.cache import get_from_cache, save_to_cache
from src.decompose import decompose_query

def main():
    init_log()
    docs = load_docs("data/docs.txt")

    query = input("Enter query: ")

    # ✅ 1. Cache Check
    cached = get_from_cache(query)
    if cached:
        print("\n[Cache Hit ⚡]")
        print("\nAnswer:\n", cached)
        return

    start_total = time.time()

    # ✅ 2. Adaptive K
    k = decide_k(query)
    print(f"[Adaptive] Using K = {k}")

    # ✅ 3. Query Decomposition
    sub_queries = decompose_query(query)
    print(f"[Decomposed Queries]: {sub_queries}")

    all_context = []

    # 🔍 Retrieval timing
    start_retrieval = time.time()

    for sub_q in sub_queries:
        results = retrieve(sub_q, k)
        all_context.extend(results)
        all_context = list(set(all_context))

    context = "\n".join(all_context)

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

    # ✅ Save to cache
    save_to_cache(query, answer)

    # ✅ Log metrics
    log_metrics(query, total_latency, len(answer))

    print(f"\n[Retrieval Time]: {retrieval_time:.2f}s")
    print(f"[Generation Time]: {generation_time:.2f}s")
    print(f"[Total Latency]: {total_latency:.2f}s")

    print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()