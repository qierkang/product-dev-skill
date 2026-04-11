# Product Dev Skill Claude Rules

1. 本仓库默认遵守 `AGENTS.md`、`SKILL.md`、`skills/product-dev/SKILL.md`、`skills/product-dev-ui/SKILL.md`。
2. 进入 UI 文档阶段时：
   - 若当前运行端可识别 `ui-ux-pro-max`，优先使用它补设计基线。
   - 若当前运行端不可识别 `ui-ux-pro-max`，唯一允许的回退路径是 `shared/references/design/`。
3. 即使当前运行端还能识别 `frontend-design` 或其他通用设计 skill，也不得把它们当成 `ui-ux-pro-max` 缺失时的默认兜底；只有用户明确要求额外设计增强时，才允许额外调用。
4. 最终产出必须继续回填到本仓 `需求文档.md` 与 `UI交互设计规范.md` 模板结构中。
