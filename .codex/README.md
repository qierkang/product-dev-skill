# Codex 适配层

这里放 Codex 侧接入 `product-dev-skill` 的说明。

第一次接手当前仓库，先看 `../START-HERE.md`。

## 当前约定

1. Codex 使用根级 `SKILL.md` 或直接进入 `skills/product-dev/SKILL.md`
2. 若任务涉及原型分析方法、阶段卡点与最小上下文加载，补读 `skills/product-dev-methods/SKILL.md`
3. 若任务进入 UI 文档阶段，补读 `skills/product-dev-ui/SKILL.md`
4. Codex 侧不单独维护第二套产品文档流程

## 重点边界

- 先执行 `doctor.sh --capability docs`
- 不涉及数据库、启动服务、部署
- 最终状态以 `stage-gate.py` 与 request 目录产物为准
