"""GPT-2 production inference wrapper.

Loads a Transformer model and exposes controlled text generation.
"""


class GPT2Inference:
    def __init__(self, model_name="gpt2"):
        self.model_name = model_name
        self.pipeline = None
        self.loaded = False

        try:
            from transformers import pipeline

            self.pipeline = pipeline(
                "text-generation",
                model=model_name,
                device=-1
            )
            self.loaded = True
        except Exception:
            self.pipeline = None

    def generate(
        self,
        prompt,
        max_new_tokens=120,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1
    ):
        if not self.pipeline:
            return {
                "text": "GPT-2 model is not loaded.",
                "status": "model_unavailable"
            }

        result = self.pipeline(
            prompt,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            repetition_penalty=repetition_penalty,
            do_sample=True
        )

        return {
            "text": result[0]["generated_text"],
            "model": self.model_name,
            "status": "generated"
        }
