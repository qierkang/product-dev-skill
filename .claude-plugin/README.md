# Claude Code 适配层

这里放 Claude Code 侧接入 `product-dev-skill` 的说明。

第一次接手当前仓库，先看 `../START-HERE.md`。

## 当前约定

1. 主入口是 `../skills/product-dev/SKILL.md`
2. UI 文档 companion 是 `../skills/product-dev-ui/SKILL.md`
3. 方法增强统一来自 `../skills/product-dev-methods/SKILL.md`
4. Claude Code 是可选运行端，不是本 skill 包的前置依赖

## 建议读取顺序

1. `../SKILL.md`
2. `../README.md`
3. `../skills/product-dev/SKILL.md`
4. `../skills/product-dev-ui/SKILL.md`

## UI 设计协同

若 Claude Code 当前环境可识别 `ui-ux-pro-max`，进入 UI 文档阶段时优先协同该外部 design skill。

若当前环境没有该 skill，则自动回退到：

- `../shared/references/design/README.md`

即使当前环境还能识别 `frontend-design` 等通用设计 skill，也不得把它们当成默认回退路径。
