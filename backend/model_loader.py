from transformers import pipeline

_generator = None


def load_model():
    global _generator
    if _generator is None:
        _generator = pipeline(
            'text-generation',
            model='gpt2'
        )
    return _generator


def generate_answer(prompt: str):
    model = load_model()
    result = model(
        prompt,
        max_length=150,
        num_return_sequences=1
    )
    return result[0]['generated_text']
