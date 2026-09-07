"""
Assistant controller
Coordinates retrieval, model generation and memory hooks.
"""

from datetime import datetime


class AssistantController:
    def __init__(self, model=None, retriever=None, memory=None):
        self.model = model
        self.retriever = retriever
        self.memory = memory

    def build_context(self, query):
        if self.retriever is None:
            return ""
        return self.retriever.search(query)

    def ask(self, query):
        context = self.build_context(query)

        prompt = query
        if context:
            prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

        if self.model:
            answer = self.model.generate(prompt)
        else:
            answer = "Model not connected yet"

        if self.memory:
            self.memory.save({
                "query": query,
                "answer": answer,
                "timestamp": datetime.utcnow().isoformat()
            })

        return {
            "answer": answer,
            "context_used": bool(context)
        }
