"""RAG + GPT-2 generation bridge.

Pipeline:
query -> retriever -> context -> GPT-2 generator
"""

from typing import List, Dict

from assistant.model.inference import GPT2Inference
from assistant.rag.pipeline import RAGPipeline


class RAGGenerator:
    def __init__(self, retriever=None, generator=None, model_name="gpt2", corpus_path="corpus"):
        self.retriever = retriever or RAGPipeline(corpus_path)
        self.generator = generator or GPT2Inference(model_name)

    def build_prompt(self, query: str, documents: List[Dict]) -> str:
        context = "\n\n".join(
            item.get("content", item.get("text", "")) for item in documents
        )

        return (
            "Context:\n"
            + context
            + "\n\nQuestion:\n"
            + query
            + "\n\nAnswer:"
        )

    def generate(self, query: str, max_length=300):
        if hasattr(self.retriever, "retrieve"):
            documents = self.retriever.retrieve(query)
        else:
            documents = self.retriever.search(query)

        prompt = self.build_prompt(query, documents)

        return {
            "response": self.generator.generate(prompt, max_length=max_length),
            "prompt": prompt,
            "sources": documents
        }
