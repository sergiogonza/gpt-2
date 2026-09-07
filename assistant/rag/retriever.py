from pathlib import Path

ROOT = Path(__file__).parent.parent / "corpus"


def load_documents():
    docs = []
    if not ROOT.exists():
        return docs
    for file in ROOT.rglob('*'):
        if file.is_file() and file.suffix in ['.txt','.md','.json','.py','.js']:
            docs.append({"file": str(file), "text": file.read_text(errors='ignore')})
    return docs


def retrieve(query, limit=3):
    docs = load_documents()
    terms = query.lower().split()
    scored=[]
    for doc in docs:
        score=sum(1 for t in terms if t in doc['text'].lower())
        scored.append((score, doc))
    scored.sort(key=lambda x:x[0], reverse=True)
    return [d for s,d in scored[:limit] if s>0]
