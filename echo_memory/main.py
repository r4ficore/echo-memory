"""Command line interface for echo-memory."""

import argparse
from pathlib import Path
from typing import Optional

from .trace_manager import TraceManager
from .replay import replay_session
from .hash_engine import generate_session_hash

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


def cmd_record(args: argparse.Namespace) -> None:
    manager = TraceManager(DATA_DIR)
    resonance = float(args.resonance) if args.resonance is not None else None
    manager.record(args.text, resonance=resonance)


def cmd_replay(args: argparse.Namespace) -> None:
    replay_session(DATA_DIR)


def cmd_emit(args: argparse.Namespace) -> None:
    session_hash = generate_session_hash(DATA_DIR)
    print(session_hash)


def cmd_reset(args: argparse.Namespace) -> None:
    manager = TraceManager(DATA_DIR)
    manager.reset()
    print('session reset')


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='echo-memory CLI')
    subparsers = parser.add_subparsers(dest='command')

    record_p = subparsers.add_parser('record', help='record a message')
    record_p.add_argument('text', help='message text')
    record_p.add_argument('--resonance', help='resonance value (0.0-1.0)', default=None)
    record_p.set_defaults(func=cmd_record)

    replay_p = subparsers.add_parser('replay', help='replay the session')
    replay_p.set_defaults(func=cmd_replay)

    emit_p = subparsers.add_parser('emit', help='generate SESSION HASH')
    emit_p.set_defaults(func=cmd_emit)

    reset_p = subparsers.add_parser('reset', help='reset the session')
    reset_p.set_defaults(func=cmd_reset)

    return parser


def main(argv: Optional[list] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
