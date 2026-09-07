import os

from transformers import AutoTokenizer, AutoModelForCausalLM

_tokenizer = None
_model = None

MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")


def get_model():
    global _tokenizer, _model

    if _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        _model.eval()

    return _tokenizer, _model


def generate(prompt, context=""):
    tokenizer, model = get_model()

    input_text = (
        "Context:\n"
        + context
        + "\n\nUser:\n"
        + prompt
        + "\n\nAssistant:"
    )

    inputs = tokenizer(input_text, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

    generated = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated[len(input_text):].strip()
