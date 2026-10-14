#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MODEL_ID="${MODEL_ID:-Qwen/Qwen3-8B}"
TARGET_DIR="${TARGET_DIR:-models/original_model/Qwen3-8B}"
PYTHON="${PYTHON:-$ROOT/.venv-verl/bin/python}"

if [[ ! -x "$PYTHON" ]]; then
  echo "[download] Python not found: $PYTHON" >&2
  echo "[download] run: bash scripts/setup_env.sh" >&2
  exit 1
fi

mkdir -p "$(dirname "$TARGET_DIR")"
"$PYTHON" -m pip show huggingface_hub >/dev/null 2>&1 || "$PYTHON" -m pip install huggingface_hub
"$PYTHON" -m huggingface_hub.commands.huggingface_cli download "$MODEL_ID" \
  --local-dir "$TARGET_DIR" \
  --local-dir-use-symlinks False

echo "[download] model ready: $ROOT/$TARGET_DIR"
