import os

class CorpusEngine:
    def __init__(self, path="../corpus_engine"):
        self.path = path

    def load(self):
        docs = []
        if os.path.exists(self.path):
            for root, _, files in os.walk(self.path):
                for file in files:
                    if file.endswith((".txt", ".md", ".json", ".py", ".js")):
                        with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                            docs.append(f.read())
        return docs


def retrieve_context(query):
    engine = CorpusEngine()
    docs = engine.load()
    matches = []

    words = query.lower().split()
    for doc in docs:
        score = sum(1 for word in words if word in doc.lower())
        if score:
            matches.append((score, doc[:1000]))

    matches.sort(reverse=True, key=lambda x: x[0])
    return "\n\n".join(item[1] for item in matches[:3])


def retrieve(query):
    return retrieve_context(query)
