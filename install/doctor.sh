#!/usr/bin/env bash
set -euo pipefail

CAPABILITY="docs"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --capability)
      CAPABILITY="${2:-docs}"
      shift 2
      ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 1
      ;;
  esac
done

echo "[doctor] capability=${CAPABILITY}"

check_cmd() {
  local cmd="$1"
  if ! command -v "${cmd}" >/dev/null 2>&1; then
    echo "[doctor][FAIL] missing command: ${cmd}" >&2
    exit 2
  fi
}

case "${CAPABILITY}" in
  docs)
    check_cmd python3
    check_cmd git
    ;;
  *)
    echo "[doctor][FAIL] unsupported capability: ${CAPABILITY}" >&2
    echo "[doctor][FAIL] supported capability: docs" >&2
    exit 3
    ;;
esac

echo "[doctor][PASS] ${CAPABILITY}"
