# echo-memory

A local CLI for recording, hashing and replaying user sessions.

## Installation

Requires Python 3.10+.
Clone the repository and run commands using `python -m echo_memory.main` or install locally with pip.

```
python -m pip install -e .
```

## Usage

```
python -m echo_memory.main record "Hello" --resonance 0.95
python -m echo_memory.main replay
python -m echo_memory.main emit
python -m echo_memory.main reset
```

The `emit` command prints a SESSION HASH based on current data files.
