#!/usr/bin/env python3
import argparse
import json
import re
from html import unescape
from pathlib import Path


KEYWORDS = ["查询", "重置", "添加", "新增", "编辑", "删除", "保存", "提交", "归档", "上传", "附件", "主表", "子表", "孙表", "必填"]
OPERATION_KEYWORDS = ["查询", "重置", "添加", "新增", "编辑", "删除", "保存", "提交", "归档", "上传", "下载", "关闭", "取消"]
STATUS_NOISE_TERMS = {"待审批", "待付款", "在借", "逾期", "已归还"}


def clean_text(html: str) -> list[str]:
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "\n", text)
    text = unescape(text)
    lines: list[str] = []
    seen: set[str] = set()
    for raw in text.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if len(line) < 2 or line in seen:
            continue
        seen.add(line)
        lines.append(line)
    return lines


def detect_page_type(title: str, lines: list[str], path: Path) -> str:
    text = " ".join([title, path.stem] + lines[:40])
    if "新增" in text:
        return "新增页"
    if "编辑" in text:
        return "编辑页"
    if "详情" in text:
        return "详情页"
    if "列表" in text or "看板" in text:
        return "列表页 / 看板页"
    return "待判断"


def detect_operations(lines: list[str]) -> list[str]:
    operations: list[str] = []
    for keyword in OPERATION_KEYWORDS:
        if any(match_operation(line, keyword) for line in lines):
            operations.append(keyword)
    return operations


def match_operation(line: str, keyword: str) -> bool:
    normalized = line.strip()
    if not normalized:
        return False
    if keyword == "查询" and normalized.startswith("查询条件"):
        return False
    if normalized == keyword:
        return True
    if normalized.startswith(keyword):
        return True
    if f"【{keyword}】" in normalized:
        return True
    if f"点击{keyword}" in normalized or f"点击【{keyword}】" in normalized:
        return True
    return False


def detect_suspected_issues(title: str, page_type: str, lines: list[str]) -> list[str]:
    issues: list[str] = []
    if "详情" in page_type and any("查询条件" in line for line in lines):
        issues.append("详情页中出现查询条件说明，疑似列表页模板残留")
    if any("删除项目" in line and "新建任务" in line for line in lines):
        issues.append("按钮说明同时出现“删除项目”和“新建任务弹框”，疑似原型文案笔误")
    if any("人员编码编码" in line for line in lines):
        issues.append("存在重复词“人员编码编码”，疑似原型文案错误")
    if "项目" in title:
        noise_hits = [line for line in lines if line in STATUS_NOISE_TERMS]
        if len(noise_hits) >= 3:
            issues.append("项目原型中出现多组疑似非项目域状态值，需确认是否为模板残留")
    return issues


def extract_summary(path: Path) -> dict:
    html = path.read_text(encoding="utf-8", errors="ignore")
    title_match = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    title = title_match.group(1).strip() if title_match else path.stem
    lines = clean_text(html)
    hits = [line for line in lines if any(keyword in line for keyword in KEYWORDS)]
    return {
        "path": str(path),
        "title": title,
        "page_type": detect_page_type(title, lines, path),
        "inputs": len(re.findall(r"<input\b", html, flags=re.I)),
        "selects": len(re.findall(r"<select\b", html, flags=re.I)),
        "textareas": len(re.findall(r"<textarea\b", html, flags=re.I)),
        "operations": detect_operations(lines),
        "suspected_issues": detect_suspected_issues(title, detect_page_type(title, lines, path), lines),
        "samples": lines[:40],
        "highlights": hits[:20],
    }


def write_markdown(output_path: Path, summaries: list[dict]) -> None:
    lines = ["# 原型解析摘要", ""]
    for item in summaries:
        lines.append(f"## {item['title']}")
        lines.append("")
        lines.append(f"- 源文件：`{item['path']}`")
        lines.append(f"- 页面类型判断：`{item['page_type']}`")
        lines.append(f"- 控件统计：`input={item['inputs']}` `select={item['selects']}` `textarea={item['textareas']}`")
        lines.append(f"- 识别到的操作词：`{' / '.join(item['operations']) if item['operations'] else '无'}`")
        lines.append("- 疑似污染 / 矛盾：")
        if item["suspected_issues"]:
            for issue in item["suspected_issues"]:
                lines.append(f"  - {issue}")
        else:
            lines.append("  - 未发现明显污染项")
        lines.append("- 关键片段：")
        for highlight in item["highlights"]:
            lines.append(f"  - {highlight}")
        lines.append("- 文本样本：")
        for sample in item["samples"][:12]:
            lines.append(f"  - {sample}")
        lines.append("")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_manifest(request_dir: Path, inputs: list[str]) -> None:
    manifest_path = request_dir / "manifest.json"
    if not manifest_path.exists():
        return
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    payload["input_assets"] = inputs
    manifest_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_assets_readme(request_dir: Path, inputs: list[str]) -> None:
    assets_dir = request_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    lines = ["# 输入资产说明", "", "当前 request 使用的原型输入资产：", ""]
    for item in inputs:
        lines.append(f"- `{item}`")
    lines.append("")
    lines.append("默认不直接复制原始 HTML 到仓库内，避免把本地原型文件一起提交。")
    (assets_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request-dir", required=True)
    parser.add_argument("--input", action="append", required=True)
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    request_dir = Path(args.request_dir)
    output_path = Path(args.output) if args.output else request_dir / "原型解析摘要.md"
    input_paths = [str(Path(item).resolve()) for item in args.input]
    summaries = [extract_summary(Path(item)) for item in input_paths]
    write_markdown(output_path, summaries)
    update_manifest(request_dir, input_paths)
    write_assets_readme(request_dir, input_paths)
    print(f"[extract-prototype-outline] wrote: {output_path}")


if __name__ == "__main__":
    main()
