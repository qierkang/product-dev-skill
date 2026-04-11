# chg-0004 harden ui fallback to internal design only

## 时间

`2026-04-12`

## 结论

`product-dev-skill` 现在把 UI fallback 规则收紧为：`ui-ux-pro-max` 缺失时，只允许回退到仓库内置 `shared/references/design/`。

## 背景

真实 Claude 隔离回归已验证当前仓库能正确走内置 fallback，但为了避免未来被 `frontend-design` 等通用设计 skill 抢路，需要把约束写得更硬、更显式。

## 本次改动

- 在 `AGENTS.md`、根级 `SKILL.md`、主入口 skill、UI skill、`design/README.md`、Claude/Codex 适配层中显式点名
- 新增根级 `CLAUDE.md`
- 明确 `frontend-design` 不属于默认兜底
- 继续保持 `ui-ux-pro-max -> shared/references/design/` 的两级路径不变

## 下一步

- 后续继续用 Claude / Codex / OpenClaw 做回归，确认不同运行端都不会擅自改用通用设计 skill
