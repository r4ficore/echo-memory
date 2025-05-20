#!/bin/bash

echo "🔁 Uruchamiam echo-memory..."

# Instalacja zależności
pip install -r requirements.txt

# Reset sesji na czysto
python -m echo_memory.main reset

# Wprowadź wpis testowy
python -m echo_memory.main record "To jest pierwszy wpis testowy" --resonance 0.96

# Odtwórz sesję
python -m echo_memory.main replay

# Wygeneruj SESSION HASH
python -m echo_memory.main emit
