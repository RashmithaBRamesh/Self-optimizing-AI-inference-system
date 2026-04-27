def decompose_query(query):
    query_lower = query.lower()

    # Handle comparison queries
    if "compare" in query_lower or "difference" in query_lower:
        parts = query_lower.replace("compare", "").replace("difference between", "").split("and")
        sub_queries = [f"What is {p.strip()}" for p in parts if p.strip()]
        return sub_queries

    # Default → no decomposition
    return [query]