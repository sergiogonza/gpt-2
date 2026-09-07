"""Production RAG + GPT-2 orchestration pipeline."""

from assistant.rag.pipeline import RAGPipeline
from assistant.model.inference import GPT2Inference


class AssistantPipeline:
    def __init__(self):
        self.rag = RAGPipeline()
        self.model = GPT2Inference()

    def chat(self, question):
        context = self.rag.build_context(question)

        prompt = (
            "Use the following context to answer.\n\n"
            "Context:\n"
            f"{context}\n\n"
            "Question:\n"
            f"{question}\n\n"
            "Answer:"
        )

        response = self.model.generate(
            prompt,
            max_new_tokens=120,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1
        )

        return {
            "question": question,
            "context": context,
            "response": response,
            "pipeline": "rag-gpt2-production"
        }
