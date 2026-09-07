"""
Prompt manager for GPT-2 + RAG context injection.
"""


class PromptManager:
    def create(self, question, context=None):
        if context:
            return (
                "Context:\n"
                + context
                + "\n\nQuestion:\n"
                + question
                + "\n\nAnswer:"
            )

        return "Question:\n" + question + "\n\nAnswer:"
