"""Text loader for Corpus Engine."""

from pathlib import Path


def load_text(path):
    file = Path(path)
    return {
        "type": "text",
        "source": str(file),
        "content": file.read_text(encoding="utf-8")
    }
