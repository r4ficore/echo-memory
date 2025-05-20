"""Utility functions for echo-memory."""

from datetime import datetime
import json
from pathlib import Path


def get_timestamp() -> str:
    """Return current timestamp in ISO format."""
    return datetime.utcnow().isoformat()


def load_json(path: Path):
    """Load JSON data from path, return empty list if file missing or empty."""
    if not path.exists():
        return []
    try:
        with path.open('r', encoding='utf-8') as fh:
            data = json.load(fh)
    except json.JSONDecodeError:
        return []
    return data


def save_json(path: Path, data):
    """Save data as JSON to path."""
    with path.open('w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2)
        fh.write('\n')
