#!/usr/bin/env python3
import argparse
import json
import os
from datetime import datetime
from pathlib import Path


TEMPLATE_MAP = {
    "需求总览模板.md": "00-需求总览.md",
    "需求文档模板.md": "需求文档.md",
    "UI交互设计模板.md": "UI交互设计规范.md",
    "manifest模板.json": "manifest.json",
    "stage-status模板.json": "stage-status.json",
}


def load_env(repo_root: Path) -> dict[str, str]:
    env_path = repo_root / ".env"
    values: dict[str, str] = {}
    if not env_path.exists():
        return values
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def render(content: str, mapping: dict[str, str]) -> str:
    result = content
    for key, value in mapping.items():
        result = result.replace(f"{{{{{key}}}}}", value)
    return result


def write_from_templates(req_dir: Path, mapping: dict[str, str], force: bool) -> None:
    template_root = Path(__file__).resolve().parents[1] / "templates"
    for template_name, output_name in TEMPLATE_MAP.items():
        target = req_dir / output_name
        if target.exists() and not force:
            continue
        content = (template_root / template_name).read_text(encoding="utf-8")
        target.write_text(render(content, mapping), encoding="utf-8")


def normalize_title(title: str, request_key: str) -> str:
    return title.strip() or request_key.replace("-", " ").strip()


def update_manifest(req_dir: Path, request_key: str, title: str, owner: str, request_type: str, platforms: list[str]) -> None:
    path = req_dir / "manifest.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["request_key"] = request_key
    payload["title"] = title
    payload["owner"] = owner
    payload["request_type"] = request_type
    payload["platforms"] = platforms or ["pc-web"]
    payload["input_assets"] = payload.get("input_assets") or []
    payload["gates"] = payload.get("gates") or {"requirement": "PENDING", "ui": "PENDING"}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_stage_status(req_dir: Path, request_key: str) -> None:
    path = req_dir / "stage-status.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["request_key"] = request_key
    payload["current_stage"] = payload.get("current_stage") or "requirement"
    payload["status"] = payload.get("status") or "IN_PROGRESS"
    payload["updated_at"] = datetime.now().isoformat(timespec="seconds")
    payload["checks"] = payload.get("checks") or {"requirement": "PENDING", "ui": "PENDING"}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request-key", required=True)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--title", default="")
    parser.add_argument("--owner", default="")
    parser.add_argument("--request-type", default="new-feature")
    parser.add_argument("--platforms", default="pc-web")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    env_values = load_env(repo_root)
    request_key = args.request_key.strip()
    title = normalize_title(args.title, request_key)
    owner = args.owner.strip() or env_values.get("PRODUCT_DEV_OWNER") or os.environ.get("PRODUCT_DEV_OWNER") or "qierkang+codex"
    now = datetime.now().strftime("%Y-%m-%d")
    mapping = {
        "REQUEST_KEY": request_key,
        "REQUEST_TITLE": title,
        "REQUEST_TYPE": args.request_type.strip(),
        "CURRENT_DATE": now,
        "OWNER": owner,
    }

    req_dir = Path(args.workspace) / request_key
    (req_dir / "assets").mkdir(parents=True, exist_ok=True)
    (req_dir / "analysis").mkdir(parents=True, exist_ok=True)
    (req_dir / "logs").mkdir(parents=True, exist_ok=True)

    write_from_templates(req_dir, mapping, args.force)

    platforms = [item.strip() for item in args.platforms.split(",") if item.strip()]
    update_manifest(req_dir, request_key, title, owner, args.request_type.strip(), platforms)
    update_stage_status(req_dir, request_key)

    print(f"[init-request] ready: {req_dir}")


if __name__ == "__main__":
    main()
