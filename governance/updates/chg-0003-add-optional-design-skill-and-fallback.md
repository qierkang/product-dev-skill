# chg-0003 add optional design skill and fallback

## 时间

`2026-04-12`

## 结论

`product-dev-skill` 已升级为“外部设计 skill 优先，内置设计参考兜底”的模式。

## 背景

此前 `product-dev-skill` 可以稳定生成需求文档和 UI 文档，但 UI 部分更偏结构化说明，缺少系统化的设计知识承接。

用户已明确希望：

- 如果运行端有 `ui-ux-pro-max`，优先借助它提升页面设计质量
- 如果运行端没有该外部 skill，仓库自身也要能继续完整输出

## 本次改动

- 新增 `shared/references/design/`
- `product-dev-ui` 增加外部设计 skill 协同规则
- `UI交互设计模板.md` 增加风格、token、动效、可访问性结构
- `ui-gate.md` 和 `stage-gate.py` 同步加强
- `README.md`、根级 `SKILL.md`、Claude/Codex 适配层同步说明该协同模式

## 验证

- 待对 `project-management-pm-recheck` 再跑一次 `ui / all` Gate 验证

## 下一步

- 若后续发现 `ui-ux-pro-max` 常给出高价值稳定输出，可继续把其中共性规则内化到本仓 `design/` 目录
