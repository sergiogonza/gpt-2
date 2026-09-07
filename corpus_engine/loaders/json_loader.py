"""JSON loader for structured knowledge."""

import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return {
        "type": "json",
        "source": path,
        "content": data
    }
