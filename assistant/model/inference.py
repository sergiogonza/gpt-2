"""GPT-2 inference wrapper.

Loads a local model when available and exposes a simple generation interface.
"""

class GPT2Inference:
    def __init__(self, model_name="gpt2"):
        self.model_name = model_name
        self.pipeline = None
        try:
            from transformers import pipeline
            self.pipeline = pipeline("text-generation", model=model_name)
        except Exception:
            self.pipeline = None

    def generate(self, prompt, max_length=200):
        if self.pipeline:
            result = self.pipeline(prompt, max_length=max_length)
            return result[0]["generated_text"]
        return "GPT-2 model is not loaded. Install dependencies and download model weights." 
