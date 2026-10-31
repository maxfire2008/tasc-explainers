#!/usr/bin/env bash
# Downloads the Kokoro TTS model (~340 MB) into models/kokoro/
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p models/kokoro
base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "models/kokoro/$f" ] || curl -L --fail -o "models/kokoro/$f" "$base/$f"
done
ls -la models/kokoro
