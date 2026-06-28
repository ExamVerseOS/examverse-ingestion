import json
from pathlib import Path

def save_json(data, path="app/outputs/debug.json"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    return path