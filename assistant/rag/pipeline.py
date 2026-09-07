"""RAG pipeline connecting retrieval with generation context."""

from pathlib import Path

class RAGPipeline:
    def __init__(self, corpus_path="corpus"):
        self.corpus_path = Path(corpus_path)

    def retrieve(self, query, limit=3):
        results = []
        if not self.corpus_path.exists():
            return results
        for file in self.corpus_path.rglob("*"):
            if file.is_file():
                try:
                    text = file.read_text(errors="ignore")
                    if any(word.lower() in text.lower() for word in query.split()):
                        results.append({"file": str(file), "content": text[:1000]})
                except Exception:
                    pass
        return results[:limit]

    def build_context(self, query):
        docs = self.retrieve(query)
        return "\n\n".join(d["content"] for d in docs)
