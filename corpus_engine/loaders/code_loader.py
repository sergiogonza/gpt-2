"""Code loader for programming repositories."""

from pathlib import Path

SUPPORTED = [
    ".py", ".js", ".ts", ".html", ".css", ".sol"
]


def load_code(path):
    file = Path(path)
    return {
        "type": "code",
        "language": file.suffix,
        "source": str(file),
        "content": file.read_text(encoding="utf-8")
    }
