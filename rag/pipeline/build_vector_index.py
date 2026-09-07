"""
Automatic Embeddings -> FAISS pipeline

Reads corpus JSON files, creates Transformer embeddings,
and builds a FAISS vector index.
"""

import json
import os
import glob
import numpy as np

from sentence_transformers import SentenceTransformer
import faiss

CORPUS_PATH = "corpus"
OUTPUT_DIR = "data"
MODEL_NAME = "all-MiniLM-L6-v2"


def load_documents():
    docs = []
    for file in glob.glob(f"{CORPUS_PATH}/**/*.json", recursive=True):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                docs.extend(data)
            else:
                docs.append(data)
    return docs


def build_index():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    documents = load_documents()
    texts = [d.get("text", str(d)) for d in documents]

    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode(texts, normalize_embeddings=True)

    vectors = np.asarray(vectors, dtype="float32")

    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    faiss.write_index(index, f"{OUTPUT_DIR}/faiss.index")

    with open(f"{OUTPUT_DIR}/metadata.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    print(f"Indexed {len(documents)} documents")


if __name__ == "__main__":
    build_index()
