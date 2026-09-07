import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

CORPUS_PATH = "corpus_engine"
OUT_DIR = "backend/vector_store"
MODEL = "all-MiniLM-L6-v2"

os.makedirs(OUT_DIR, exist_ok=True)

encoder = SentenceTransformer(MODEL)

documents = []

for root, _, files in os.walk(CORPUS_PATH):
    for file in files:
        if file.endswith((".txt", ".md", ".json", ".py", ".js")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if content.strip():
                        documents.append({
                            "source": path,
                            "content": content[:3000]
                        })
            except Exception:
                continue

if not documents:
    raise RuntimeError("No corpus documents found")

texts = [d["content"] for d in documents]

vectors = encoder.encode(
    texts,
    normalize_embeddings=True
).astype("float32")

index = faiss.IndexFlatIP(vectors.shape[1])
index.add(vectors)

faiss.write_index(
    index,
    os.path.join(OUT_DIR, "index.faiss")
)

with open(os.path.join(OUT_DIR, "metadata.json"), "w", encoding="utf-8") as f:
    json.dump(
        {
            "model": MODEL,
            "count": len(documents),
            "documents": documents
        },
        f,
        ensure_ascii=False,
        indent=2
    )

print("FAISS index created:", len(documents), "documents")
