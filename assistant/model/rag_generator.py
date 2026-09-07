"""
RAG + GPT-2 generation bridge.

Pipeline:
query -> retriever -> context -> GPT-2 generator
"""

from typing import List, Dict


class RAGGenerator:
    def __init__(self, retriever=None, generator=None):
        self.retriever = retriever
        self.generator = generator

    def build_prompt(self, query: str, documents: List[Dict]) -> str:
        context = "\n\n".join(
            item.get("text", "") for item in documents
        )

        return (
            "Context:\n"
            + context
            + "\n\nQuestion:\n"
            + query
            + "\n\nAnswer:"
        )

    def generate(self, query: str):
        documents = []

        if self.retriever:
            documents = self.retriever.search(query)

        prompt = self.build_prompt(query, documents)

        if self.generator:
            return self.generator.generate(prompt)

        return {
            "prompt": prompt,
            "sources": documents,
            "status": "generator_not_loaded"
        }
