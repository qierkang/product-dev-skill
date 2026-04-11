#!/usr/bin/env python3
import argparse
import json
from datetime import datetime
from pathlib import Path


REQUIRED_FILES = {
    "requirement": ["00-需求总览.md", "需求文档.md", "manifest.json"],
    "ui": ["需求文档.md", "UI交互设计规范.md", "stage-status.json"],
}

REQUIRED_MARKERS = {
    "00-需求总览.md": ["输入资产", "页面清单", "待确认项"],
    "需求文档.md": ["业务背景", "核心目标", "功能模块", "表单定义", "业务规则"],
    "UI交互设计规范.md": [
        "设计策略与风格方向",
        "设计 Token 与组件策略",
        "页面结构与操作路径",
        "状态反馈与动效规范",
        "表单校验与联动",
        "状态与按钮显隐",
        "可访问性与响应式要求",
        "验收要点",
    ],
}

STAGES = ["requirement", "ui"]

PLACEHOLDER_SNIPPETS = [
    "[待补充]",
    "[页面原型来源]",
    "[页面A]",
    "[目标1]",
    "[目标2]",
    "[目标3]",
    "[待确认项1]",
    "[待确认项2]",
    "[待确认项3]",
    "[列表页 / 详情页 / 弹窗 / Tab页]",
    "[单表 / 主子表 / 主子孙表]",
]


def validate_markers(path: Path, markers: list[str]) -> list[str]:
    content = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if len(content.strip()) < 120:
        issues.append(f"{path.name} 内容过少，疑似未填写")
    if path.suffix == ".md" and "#" not in content:
        issues.append(f"{path.name} 缺少 Markdown 标题")
    for marker in markers:
        if marker not in content:
            issues.append(f"{path.name} 缺少关键内容：{marker}")
    for snippet in PLACEHOLDER_SNIPPETS:
        if snippet in content:
            issues.append(f"{path.name} 仍包含模板占位：{snippet}")
    return issues


def validate_manifest(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [f"{path.name} 不是合法 JSON"]
    for key in ["request_key", "title", "owner", "current_stage"]:
        if not payload.get(key):
            issues.append(f"{path.name} 缺少字段：{key}")
    return issues


def validate_stage_status(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [f"{path.name} 不是合法 JSON"]
    for key in ["request_key", "current_stage", "status", "checks"]:
        if payload.get(key) in (None, "", {}):
            issues.append(f"{path.name} 缺少字段：{key}")
    if payload.get("current_stage") and payload["current_stage"] not in STAGES:
        issues.append(f"{path.name} current_stage 非法：{payload['current_stage']}")
    return issues


def check_stage(request_dir: Path, stage: str) -> dict:
    missing: list[str] = []
    issues: list[str] = []
    for file_name in REQUIRED_FILES[stage]:
        path = request_dir / file_name
        if not path.exists():
            missing.append(file_name)
            continue
        if file_name in REQUIRED_MARKERS:
            issues.extend(validate_markers(path, REQUIRED_MARKERS[file_name]))
        if file_name == "manifest.json":
            issues.extend(validate_manifest(path))
        if file_name == "stage-status.json":
            issues.extend(validate_stage_status(path))
    return {"stage": stage, "pass": not missing and not issues, "missing": missing, "issues": issues}


def update_stage_status(request_dir: Path, stage: str, passed: bool) -> None:
    path = request_dir / "stage-status.json"
    now = datetime.now().isoformat(timespec="seconds")
    payload = {}
    if path.exists():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            payload = {}
    checks = payload.get("checks")
    if not isinstance(checks, dict):
        checks = {"requirement": "PENDING", "ui": "PENDING"}
    checks[stage] = "PASSED" if passed else "FAILED"
    payload["request_key"] = payload.get("request_key") or request_dir.name
    payload["current_stage"] = stage
    payload["current_task"] = f"执行 {stage} gate"
    payload["status"] = "PASSED" if all(checks.get(s) == "PASSED" for s in STAGES) else "IN_PROGRESS"
    if not passed:
        payload["status"] = "FAILED"
        payload["next_action"] = f"修复 {stage} 阶段缺失项"
    elif stage == "requirement":
        payload["next_action"] = "补充 UI交互设计规范"
    else:
        payload["next_action"] = "已通过全部 Gate，可沉淀示例或进入下游流程"
    payload["checks"] = checks
    payload["updated_at"] = now
    history = payload.get("history")
    if not isinstance(history, list):
        history = []
    history.append({"stage": stage, "pass": passed, "checked_at": now})
    payload["history"] = history[-20:]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_manifest(request_dir: Path, stage: str, passed: bool) -> None:
    path = request_dir / "manifest.json"
    if not path.exists():
        return
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    gates = payload.get("gates")
    if not isinstance(gates, dict):
        gates = {"requirement": "PENDING", "ui": "PENDING"}
    gates[stage] = "PASSED" if passed else "FAILED"
    payload["gates"] = gates
    payload["current_stage"] = stage
    payload["status"] = "ready" if all(gates.get(s) == "PASSED" for s in STAGES) else payload.get("status", "draft")
    if not passed:
        payload["status"] = "needs_work"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request-dir", required=True)
    parser.add_argument("--stage", required=True, choices=STAGES + ["all"])
    args = parser.parse_args()

    request_dir = Path(args.request_dir)
    if args.stage == "all":
        results = [check_stage(request_dir, stage) for stage in STAGES]
        overall = all(item["pass"] for item in results)
        for result in results:
            update_stage_status(request_dir, result["stage"], result["pass"])
            update_manifest(request_dir, result["stage"], result["pass"])
        final = {"stage": "all", "pass": overall, "results": results}
        print(json.dumps(final, ensure_ascii=False))
        if not overall:
            raise SystemExit(2)
        return

    result = check_stage(request_dir, args.stage)
    update_stage_status(request_dir, args.stage, result["pass"])
    update_manifest(request_dir, args.stage, result["pass"])
    print(json.dumps(result, ensure_ascii=False))
    if not result["pass"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
