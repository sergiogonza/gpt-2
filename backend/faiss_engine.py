import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "backend/vector_store/index.faiss"
META_PATH = "backend/vector_store/metadata.json"

class FaissEngine:
    def __init__(self):
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.metadata = []

    def load(self):
        if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            with open(META_PATH, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)
            return True
        return False

    def search(self, query, limit=3):
        if self.index is None:
            self.load()

        if self.index is None:
            return []

        vector = self.encoder.encode([query]).astype("float32")
        distances, ids = self.index.search(vector, limit)

        results = []
        for i in ids[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i])

        return results

engine = FaissEngine()
