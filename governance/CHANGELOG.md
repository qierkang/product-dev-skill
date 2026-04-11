# CHANGELOG

## 2026-04-11

- 初始化 `product-dev-skill` 骨架
- 从 `picasso-dev-skill` 继承需求文档与 UI 交互模板基线
- 从 `product-delivery-skill` 继承轻量初始化与 Gate 脚本思路
- 收缩为 `原型分析 -> 需求文档 -> UI交互文档 -> Gate` 最小链路
- 完成 `project-management-pm-recheck` 第二轮真实陪跑复验并沉淀到 `examples/`
- 强化 `extract-prototype-outline.py`，补操作词误识别修正与污染识别结果复核
- 修正 `需求总览模板.md` 默认阶段口径，避免初始化即显示完成态

## 2026-04-12

- 新增 `shared/references/design/`，作为 `ui-ux-pro-max` 缺失时的内置设计兜底层
- `product-dev-ui`、主入口、README、Claude/Codex 适配层已明确“外部设计 skill 优先，内置规则兜底”
- `UI交互设计模板.md` 与 UI Gate 已升级，要求补齐风格方向、token、动效与可访问性结构
- 真实 Claude 隔离回归后，已显式禁止把 `frontend-design` 之类通用设计 skill 当成默认回退路径
- 新增根级 `CLAUDE.md`，把 UI fallback 规则直接前置给 Claude 运行端
