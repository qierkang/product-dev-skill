#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[product-dev-skill] setup start"
mkdir -p "${ROOT_DIR}/workspace/requests"
mkdir -p "${ROOT_DIR}/workspace/simulations"
mkdir -p "${ROOT_DIR}/governance/updates"
mkdir -p "${ROOT_DIR}/governance/decisions"
mkdir -p "${ROOT_DIR}/examples"

if [[ ! -f "${ROOT_DIR}/.env" && -f "${ROOT_DIR}/.env.example" ]]; then
  cp "${ROOT_DIR}/.env.example" "${ROOT_DIR}/.env"
  echo "[product-dev-skill] created .env from .env.example"
fi

echo "[product-dev-skill] setup done"
