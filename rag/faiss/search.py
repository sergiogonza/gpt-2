import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX='../../data/faiss.index'
META='../../data/faiss-meta.json'

model=SentenceTransformer('all-MiniLM-L6-v2')

index=faiss.read_index(INDEX)

with open(META,'r',encoding='utf-8') as f:
    docs=json.load(f)


def search(query,top_k=5):
    vector=model.encode([query],normalize_embeddings=True)
    vector=np.array(vector).astype('float32')

    scores,ids=index.search(vector,top_k)

    return [
        {
            'score':float(scores[0][i]),
            'document':docs[idx]
        }
        for i,idx in enumerate(ids[0])
        if idx >= 0
    ]

if __name__=='__main__':
    print(search('inteligencia artificial'))
