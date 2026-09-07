import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

CORPUS='../../data/vector-index.json'
INDEX='../../data/faiss.index'
META='../../data/faiss-meta.json'

model=SentenceTransformer('all-MiniLM-L6-v2')

def main():
    with open(CORPUS,'r',encoding='utf-8') as f:
        docs=json.load(f)

    texts=[d['text'] for d in docs]
    vectors=model.encode(texts,normalize_embeddings=True)
    vectors=np.array(vectors).astype('float32')

    index=faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    faiss.write_index(index,INDEX)

    with open(META,'w',encoding='utf-8') as f:
        json.dump(docs,f,indent=2,ensure_ascii=False)

if __name__=='__main__':
    main()
