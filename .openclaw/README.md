# OpenClaw 适配层

这里放 OpenClaw 总控侧接入 `product-dev-skill` 的说明。

第一次接手当前仓库，先看 `../START-HERE.md`。

## 当前约定

1. OpenClaw 总控调度产品原型文档化任务时，统一调用 `product-dev`
2. 若要判断方法层是否齐备，可查 `skills/product-dev-methods/`
3. 适配层只做调度和识别说明，不复制主流程模板
4. 即使没有 Claude Code 或 Codex，OpenClaw 也可以独立使用这套 skill

## 总控识别建议

- 主流程：`skills/product-dev/`
- UI 文档：`skills/product-dev-ui/`
- 方法层：`skills/product-dev-methods/`
- 维护治理：`skills/product-dev-maintainer/`、`governance/`
