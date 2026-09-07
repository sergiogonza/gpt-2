import os
import json
import faiss
from sentence_transformers import SentenceTransformer

CORPUS_PATH = "corpus_engine"
OUT_DIR = "backend/vector_store"

os.makedirs(OUT_DIR, exist_ok=True)

encoder = SentenceTransformer("all-MiniLM-L6-v2")

documents = []

for root, _, files in os.walk(CORPUS_PATH):
    for file in files:
        if file.endswith((".txt", ".md", ".json", ".py", ".js")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    documents.append({
                        "source": path,
                        "content": f.read()[:2000]
                    })
            except Exception:
                pass

texts = [d["content"] for d in documents]

vectors = encoder.encode(texts).astype("float32")

index = faiss.IndexFlatIP(vectors.shape[1])
index.add(vectors)

faiss.write_index(index, OUT_DIR + "/index.faiss")

with open(OUT_DIR + "/metadata.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, ensure_ascii=False)

print("FAISS index created:", len(documents), "documents")
