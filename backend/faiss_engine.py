import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "backend/vector_store/index.faiss"
META_PATH = "backend/vector_store/metadata.json"


class FaissEngine:
    def __init__(self):
        self.encoder = None
        self.index = None
        self.metadata = []

    def load_encoder(self):
        if self.encoder is None:
            self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        return self.encoder

    def load(self):
        if self.index is not None:
            return True

        if not (os.path.exists(INDEX_PATH) and os.path.exists(META_PATH)):
            return False

        self.index = faiss.read_index(INDEX_PATH)

        with open(META_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict) and "documents" in data:
            self.metadata = data["documents"]
        else:
            self.metadata = data

        return True

    def search(self, query, limit=3):
        if not self.load():
            return []

        encoder = self.load_encoder()

        vector = encoder.encode(
            [query],
            normalize_embeddings=True
        ).astype("float32")

        distances, ids = self.index.search(vector, limit)

        results = []
        for position, idx in enumerate(ids[0]):
            if idx >= 0 and idx < len(self.metadata):
                item = self.metadata[idx]
                item["score"] = float(distances[0][position])
                results.append(item)

        return results


engine = FaissEngine()
