"""Replay session dialog from trace file."""

from pathlib import Path
from .utils import load_json


def replay_session(data_dir: Path) -> None:
    """Print the recorded session in a dialog style."""
    trace = load_json(data_dir / 'trace.json')
    for entry in trace:
        role = entry.get('role', 'user')
        text = entry.get('text', '')
        timestamp = entry.get('timestamp', '')
        resonance = entry.get('resonance')
        line = f"[{timestamp}] {role}: {text}"
        if resonance is not None:
            line += f" (resonance={resonance:.2f})"
        print(line)
