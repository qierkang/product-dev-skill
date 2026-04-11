# Product Dev Skill 约定

1. 所有回复优先使用中文简体。
2. 统一从 `skills/product-dev/SKILL.md` 作为主入口进入。
3. 需求运行产物默认写入 `workspace/requests/<request-key>/`。
4. 示例沉淀默认写入 `examples/<request-key>/`，前提是当前 request 已通过 `stage-gate.py --stage all`。
5. 当前 skill 只覆盖：`原型分析 -> 需求文档 -> UI交互文档 -> Gate`。
6. 进入任何真实产出前，先执行 `bash install/doctor.sh --capability docs`。
7. 模板以 `shared/templates/需求文档模板.md` 为核心基线，不能自行降级成口语化简版文档。
8. 原型中若已标注 `主表 / 子表 / 孙表`，需求文档必须保留层级，不得合并丢失。
9. 不在模板、README、skill 中写死个人宿主机路径；目录差异通过 `profiles/` 与 `.env` 管理。
10. `workspace/` 为运行区，默认不提交；`governance/` 为维护区，需要提交。
11. 方法论增强统一由 `skills/product-dev-methods/SKILL.md` 提供。
12. `.claude-plugin/`、`.codex/`、`.opencode/`、`.openclaw/` 为运行端适配层，不复制第二套主流程。
