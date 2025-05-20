from pathlib import Path
from echo_memory.hash_engine import hash_text, generate_session_hash
from echo_memory.trace_manager import TraceManager

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'

def test_hash_text():
    assert hash_text('test') == hash_text('test')


def test_generate_session_hash(tmp_path):
    data_dir = tmp_path
    for name in ('trace.json', 'payload.json', 'presence_log.json'):
        (data_dir / name).write_text('[]')
    session_hash1 = generate_session_hash(data_dir)
    # writing the same content should result in same hash
    session_hash2 = generate_session_hash(data_dir)
    assert session_hash1 == session_hash2


def test_trace_manager_record(tmp_path):
    data_dir = tmp_path
    manager = TraceManager(data_dir)
    manager.record('hello', resonance=0.95)
    assert (data_dir / 'trace.json').exists()
    assert (data_dir / 'payload.json').exists()
    assert (data_dir / 'presence_log.json').exists()
    traces = (data_dir / 'trace.json').read_text()
    assert 'hello' in traces
