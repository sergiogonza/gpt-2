# Embeddings -> FAISS Pipeline

Flow:

corpus JSON

```
JSON documents
      |
      v
Sentence Transformer
      |
      v
Embedding vectors
      |
      v
FAISS IndexFlatIP
      |
      v
faiss.index + metadata.json
```

Run:

```bash
pip install -r requirements.txt
python build_vector_index.py
```

Default model:

`all-MiniLM-L6-v2`
