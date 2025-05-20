"""Trace management for echo-memory."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Dict

from .utils import get_timestamp, load_json, save_json
from .hash_engine import hash_text


@dataclass
class TraceEntry:
    """Represents a single trace entry."""

    timestamp: str
    role: str
    text: str
    resonance: Optional[float] = None

    def to_dict(self) -> Dict:
        data = {
            "timestamp": self.timestamp,
            "role": self.role,
            "text": self.text,
        }
        if self.resonance is not None:
            data["resonance"] = self.resonance
        return data


class TraceManager:
    """Manage trace and payload persistence."""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.trace_path = data_dir / "trace.json"
        self.payload_path = data_dir / "payload.json"
        self.presence_path = data_dir / "presence_log.json"

    def _load_traces(self) -> List[Dict]:
        return load_json(self.trace_path)

    def _load_payload(self) -> List[str]:
        return load_json(self.payload_path)

    def _load_presence(self) -> List[Dict]:
        return load_json(self.presence_path)

    def record(self, text: str, role: str = "user", resonance: Optional[float] = None) -> None:
        entry = TraceEntry(timestamp=get_timestamp(), role=role, text=text, resonance=resonance)
        traces = self._load_traces()
        traces.append(entry.to_dict())
        save_json(self.trace_path, traces)

        payload = self._load_payload()
        payload.append(hash_text(text))
        save_json(self.payload_path, payload)

        if resonance is not None and resonance >= 0.9:
            presence = self._load_presence()
            presence.append(entry.to_dict())
            save_json(self.presence_path, presence)

    def reset(self) -> None:
        for path in (self.trace_path, self.payload_path, self.presence_path):
            save_json(path, [])
