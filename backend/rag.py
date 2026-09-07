import os

class CorpusEngine:
    def __init__(self, path="corpus"):
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


def retrieve(query):
    return ""
