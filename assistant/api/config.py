import os

MODE = os.getenv("ASSISTANT_MODE", "local")

CONFIG = {
    "mode": MODE,
    "enable_rag": True,
    "enable_memory": True,
    "enable_feedback": True
}
