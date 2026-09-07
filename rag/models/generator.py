from .gpt2_loader import load_model


_model = None
_tokenizer = None


def generate(prompt, max_length=100):
    global _model, _tokenizer

    if _model is None:
        _model, _tokenizer = load_model()

    inputs = _tokenizer(prompt, return_tensors="pt")

    output = _model.generate(
        **inputs,
        max_length=max_length,
        do_sample=True,
        temperature=0.7,
        pad_token_id=_tokenizer.eos_token_id
    )

    return _tokenizer.decode(output[0], skip_special_tokens=True)
