from pathlib import Path
import json

CORPUS = Path('corpus_engine')


def load_documents():
    docs=[]
    if not CORPUS.exists():
        return docs
    for file in CORPUS.rglob('*'):
        if file.suffix in ['.txt','.json','.md']:
            try:
                docs.append(file.read_text(encoding='utf-8'))
            except Exception:
                pass
    return docs


def retrieve_context(query, limit=3):
    docs = load_documents()
    matches=[]
    q=query.lower()
    for d in docs:
        score=sum(1 for token in q.split() if token in d.lower())
        if score:
            matches.append({'score':score,'text':d[:1000]})
    matches.sort(key=lambda x:x['score'], reverse=True)
    return matches[:limit]
