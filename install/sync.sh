#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ROOT_DIR}/.env"
TARGET="${1:-all}"
SKILL_NAME="${SKILL_NAME:-product-dev-skill}"

if [[ -f "${ENV_FILE}" ]]; then
  # shellcheck disable=SC1090
  source "${ENV_FILE}"
fi

TARGET_CODEX_SKILLS_DIR="${TARGET_CODEX_SKILLS_DIR:-$HOME/.codex/skills}"
TARGET_CLAUDE_SKILLS_DIR="${TARGET_CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
TARGET_OPENCLAW_SKILLS_DIR="${TARGET_OPENCLAW_SKILLS_DIR:-$HOME/.openclaw/skills}"
TARGET_OPENCODE_SKILLS_DIR="${TARGET_OPENCODE_SKILLS_DIR:-$HOME/.opencode/skills}"

sync_one() {
  local runtime="$1"
  local target_dir="$2"
  mkdir -p "${target_dir}"
  rsync -a \
    --delete \
    --exclude ".git/" \
    --exclude ".env" \
    --exclude "workspace/requests/" \
    --exclude "workspace/simulations/" \
    --exclude ".DS_Store" \
    "${ROOT_DIR}/" "${target_dir}/${SKILL_NAME}/"
  echo "[sync][PASS] ${runtime} -> ${target_dir}/${SKILL_NAME}"
}

case "${TARGET}" in
  codex)
    sync_one "codex" "${TARGET_CODEX_SKILLS_DIR}"
    ;;
  claude)
    sync_one "claude" "${TARGET_CLAUDE_SKILLS_DIR}"
    ;;
  openclaw)
    sync_one "openclaw" "${TARGET_OPENCLAW_SKILLS_DIR}"
    ;;
  opencode)
    sync_one "opencode" "${TARGET_OPENCODE_SKILLS_DIR}"
    ;;
  all)
    sync_one "codex" "${TARGET_CODEX_SKILLS_DIR}"
    sync_one "claude" "${TARGET_CLAUDE_SKILLS_DIR}"
    sync_one "openclaw" "${TARGET_OPENCLAW_SKILLS_DIR}"
    sync_one "opencode" "${TARGET_OPENCODE_SKILLS_DIR}"
    ;;
  *)
    echo "[sync][FAIL] unsupported target: ${TARGET}" >&2
    echo "[sync][FAIL] usage: bash install/sync.sh [all|codex|claude|openclaw|opencode]" >&2
    exit 2
    ;;
esac
