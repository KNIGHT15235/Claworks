#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-.venv-verl}"

"$PYTHON_BIN" -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install -U pip setuptools wheel

"$VENV_DIR/bin/python" -m pip install -e ".[monitoring]"
"$VENV_DIR/bin/python" -m pip install -e "verl/upstream[vllm]"
"$VENV_DIR/bin/python" -m pip install pandas pyarrow transformers accelerate sentencepiece

echo "[setup] environment ready: $ROOT/$VENV_DIR"
echo "[setup] next: cp .env.example .env, fill keys, then run training scripts"
