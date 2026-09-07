from transformers import pipeline

_generator = None

def get_model():
    global _generator
    if _generator is None:
        _generator = pipeline("text-generation", model="gpt2")
    return _generator


def generate(prompt):
    model = get_model()
    result = model(prompt, max_length=120, num_return_sequences=1)
    return result[0]["generated_text"]
