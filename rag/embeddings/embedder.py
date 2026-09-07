from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def create_embeddings(texts):
    vectors = model.encode(
        texts,
        normalize_embeddings=True
    )
    return np.asarray(vectors)


if __name__ == "__main__":
    docs = [
        "RAG recupera información antes de generar una respuesta",
        "GPT-2 es un modelo Transformer de lenguaje"
    ]

    embeddings = create_embeddings(docs)
    print(embeddings.shape)
