# Codex 适配层

这里放 Codex 侧接入 `product-dev-skill` 的说明。

第一次接手当前仓库，先看 `../START-HERE.md`。

## 当前约定

1. Codex 使用根级 `SKILL.md` 或直接进入 `skills/product-dev/SKILL.md`
2. 若任务涉及原型分析方法、阶段卡点与最小上下文加载，补读 `skills/product-dev-methods/SKILL.md`
3. 若任务进入 UI 文档阶段，补读 `skills/product-dev-ui/SKILL.md`
4. Codex 侧不单独维护第二套产品文档流程

## UI 设计协同

若 Codex 当前环境可识别 `ui-ux-pro-max`，UI 阶段优先协同它输出设计基线。

若不可识别，则自动回退到：

- `shared/references/design/README.md`

即使当前环境还能识别 `frontend-design` 等通用设计 skill，也不得把它们当成默认回退路径。

## 重点边界

- 先执行 `doctor.sh --capability docs`
- 不涉及数据库、启动服务、部署
- 最终状态以 `stage-gate.py` 与 request 目录产物为准
