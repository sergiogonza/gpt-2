import os
import json

try:
    from faiss_engine import engine as faiss_engine
    FAISS_AVAILABLE = True
except Exception:
    FAISS_AVAILABLE = False

try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    SEMANTIC_AVAILABLE = True
except Exception:
    SEMANTIC_AVAILABLE = False


class CorpusEngine:
    def __init__(self, path="../corpus_engine"):
        self.path = path
        self.documents = []
        self.encoder = None

    def load(self):
        if self.documents:
            return self.documents

        docs = []
        if os.path.exists(self.path):
            for root, _, files in os.walk(self.path):
                for file in files:
                    if file.endswith((".txt", ".md", ".json", ".py", ".js")):
                        full = os.path.join(root, file)
                        try:
                            with open(full, "r", encoding="utf-8", errors="ignore") as f:
                                docs.append({"source": full, "content": f.read()})
                        except Exception:
                            pass

        self.documents = docs
        return docs

    def semantic_search(self, query, limit=3):
        docs = self.load()

        if not docs:
            return []

        if not SEMANTIC_AVAILABLE:
            return docs[:limit]

        if self.encoder is None:
            self.encoder = SentenceTransformer("all-MiniLM-L6-v2")

        texts = [d["content"][:1000] for d in docs]
        vectors = self.encoder.encode(texts)
        query_vector = self.encoder.encode([query])[0]

        scores = []
        for index, vector in enumerate(vectors):
            score = float(np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector)))
            scores.append((score, docs[index]))

        scores.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scores[:limit]]


def retrieve_context(query):
    # Primero intenta usar FAISS persistente
    if FAISS_AVAILABLE:
        try:
            results = faiss_engine.search(query, limit=3)
            if results:
                return "\n\n".join(
                    item.get("content", "")[:1000]
                    for item in results
                )
        except Exception:
            pass

    # Fallback al motor semántico dinámico
    engine = CorpusEngine()
    results = engine.semantic_search(query)

    return "\n\n".join(
        item["content"][:1000]
        for item in results
    )


def retrieve(query):
    return retrieve_context(query)
