from transformers import pipeline

_generator = None

def get_model():
    global _generator
    if _generator is None:
        _generator = pipeline("text-generation", model="gpt2")
    return _generator


def generate(prompt, context=""):
    model = get_model()
    full_prompt = f"Context:\n{context}\n\nQuestion:\n{prompt}\n\nAnswer:"
    result = model(full_prompt, max_length=200, num_return_sequences=1)
    return result[0]["generated_text"]
