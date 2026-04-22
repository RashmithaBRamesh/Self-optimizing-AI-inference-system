from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from src.config import TOP_K

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("data/index.faiss")

def retrieve(query, docs, k=TOP_K):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)

    return [docs[i] for i in indices[0]]