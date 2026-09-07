"""Persistent lightweight memory store."""

import json
from pathlib import Path


class MemoryStore:
    def __init__(self, path="memory.json"):
        self.path = Path(path)

    def save(self, item):
        data = self.load()
        data.append(item)
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    def load(self):
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text())
