from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_docs(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def create_index(docs):
    embeddings = model.encode(docs)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return index

def save_index(index, path="data/index.faiss"):
    faiss.write_index(index, path)

if __name__ == "__main__":
    docs = load_docs("data/docs.txt")
    index = create_index(docs)
    save_index(index)
    print("✅ FAISS index created")