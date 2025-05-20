"""Hash generation utilities for echo-memory."""

import hashlib
from pathlib import Path


def hash_text(text: str) -> str:
    """Return SHA-256 hex digest for given text."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def generate_session_hash(data_dir: Path) -> str:
    """Generate a session hash based on contents of data files in data_dir."""
    contents = []
    for name in ('trace.json', 'payload.json', 'presence_log.json'):
        path = data_dir / name
        contents.append((path.read_text(encoding='utf-8') if path.exists() else ''))
    joined = ''.join(contents).encode('utf-8')
    return hashlib.sha256(joined).hexdigest()
