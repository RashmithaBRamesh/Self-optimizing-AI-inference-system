from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from src.config import TOP_K

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index
index = faiss.read_index("data/index.faiss")

# Load documents
def load_docs(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]

docs = load_docs("data/docs.txt")

# Setup BM25
tokenized_docs = [doc.split() for doc in docs]
bm25 = BM25Okapi(tokenized_docs)

def get_dynamic_k(query):
    length = len(query.split())

    if length <= 3:
        return 2
    elif length <= 7:
        return 4
    else:
        return 6


def hybrid_retrieve(query, k):
    # Vector search
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)
    vector_results = [(docs[i], distances[0][idx]) for idx, i in enumerate(indices[0])]

    # Keyword search
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)
    top_bm25_indices = np.argsort(bm25_scores)[-k:]
    keyword_results = [(docs[i], bm25_scores[i]) for i in top_bm25_indices]

    return vector_results, keyword_results

def rerank(vector_results, keyword_results):
    combined_scores = {}

    # Normalize + combine
    for doc, score in vector_results:
        combined_scores[doc] = combined_scores.get(doc, 0) + (1 / (1 + score))  # lower distance = better

    for doc, score in keyword_results:
        combined_scores[doc] = combined_scores.get(doc, 0) + score

    # Sort by final score
    ranked = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in ranked]

# Final retrieve function
def retrieve(query):
    k = get_dynamic_k(query)

    vector_results, keyword_results = hybrid_retrieve(query, k)
    ranked_docs = rerank(vector_results, keyword_results)

    return [doc for doc in ranked_docs if len(doc) > 10][:k]