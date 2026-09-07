from transformers import GPT2LMHeadModel, GPT2Tokenizer

MODEL_NAME = "gpt2"


def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
    model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
    model.eval()
    return model, tokenizer
