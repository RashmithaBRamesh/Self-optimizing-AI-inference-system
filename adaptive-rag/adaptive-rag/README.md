# Adaptive RAG Inference System

## 📌 Overview

This project implements an **Adaptive Retrieval-Augmented Generation (RAG) system** that dynamically optimizes its behavior at inference time based on query complexity, latency, and feedback signals.

The system combines:

- Semantic search (FAISS)
- Keyword search (BM25)
- Adaptive decision-making
- Feedback-driven optimization

---

## 🏗️ Architecture Diagram

User Query
↓
[ Cache Layer ⚡ ]
↓ (if miss)
[ Query Decomposition 🧠 ]
↓
[ Adaptive Decision Layer ]
↓
├── Dynamic Top-K Selection
├── Latency Awareness
└── Query Complexity Analysis
↓
[ Hybrid Retrieval ]
├── FAISS (Vector Search)
└── BM25 (Keyword Search)
↓
[ Re-ranking Layer ]
↓
[ Context Builder ]
↓
[ LLM (tinyllama via Ollama) ]
↓
Generated Answer
↓
[ Feedback Logger ]
↓
[ Cache Storage ]

---

## ⚙️ Features

### ✅ Core Features

- Document ingestion and FAISS indexing
- Query → Retrieve → Generate pipeline
- Hybrid retrieval (semantic + keyword)
- Re-ranking of retrieved results

### 🔥 Adaptive Features

- Dynamic Top-K based on query complexity
- Latency-aware retrieval adjustment
- Feedback loop using:
  - latency
  - answer length (quality proxy)

### 🚀 Bonus Features

- Query decomposition (multi-step queries)
- In-memory caching layer
- Performance measurement (P50 / P95 latency)

---

## 🧠 Design Decisions

### 1. FAISS for Vector Search

Chosen for fast and efficient similarity search on embeddings.

### 2. SentenceTransformers (MiniLM)

Used for lightweight and fast embeddings suitable for local systems.

### 3. Hybrid Retrieval (FAISS + BM25)

Combines:

- semantic understanding (FAISS)
- exact keyword matching (BM25)

### 4. Rule-Based Adaptive Layer

Simple heuristics used instead of ML models to:

- reduce complexity
- avoid training requirements

### 5. tinyllama (Local LLM)

Used due to hardware constraints:

- low memory usage
- fast inference

---

## ⚖️ Tradeoffs

| Decision | Tradeoff |

|----------|---------|
| tinyllama | Lower answer quality vs large models |
| Rule-based adaptation | Simpler but less accurate than ML |
| In-memory cache | Not persistent across runs |
| Heuristic feedback | Not true user feedback |

---

## ▶️ How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Create index

python src/ingest.py

### 3. Run system

python main.py

---

## 📊 Performance Metrics

- Tracks:

  - Retrieval time
  - Generation time
  - Total latency

- Computes:
  - P50 latency
  - P95 latency

Run:
python analyze.py

---

## 🧩 Example Queries

- What is FAISS?
- Explain machine learning
- Compare FAISS and machine learning

---

## 📌 Conclusion

This system demonstrates how adaptive logic at inference time can balance:

- performance (latency)
- quality (retrieval depth)

without requiring model training.

### Visualization Dashboard

The system includes a dashboard for monitoring:

- latency trends
- answer quality
- adaptive K usage
- cache effectiveness
