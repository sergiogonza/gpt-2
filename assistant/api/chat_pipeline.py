"""Main assistant orchestration pipeline."""

from assistant.rag.pipeline import RAGPipeline
from assistant.model.inference import GPT2Inference

class AssistantPipeline:
    def __init__(self):
        self.rag = RAGPipeline()
        self.model = GPT2Inference()

    def chat(self, question):
        context = self.rag.build_context(question)
        prompt = f"Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"
        return self.model.generate(prompt)
