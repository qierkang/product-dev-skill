# project-management-pm-recheck 示例

这是 `product-dev-skill` 针对同一组项目管理原型做的第二轮真实复验样例。

## 示例目的

1. 验证模板去噪后，初始化的需求文档不再带入无关业务说明
2. 验证原型解析摘要已补充操作词识别、污染识别和输入资产说明
3. 验证回填后的需求文档和 UI 交互文档可再次通过 `requirement / ui / all` 三道 Gate

## 原始输入

- `prototype-inputs/project-board.html`
- `prototype-inputs/project-detail-manage.html`
- `prototype-inputs/project-detail-create.html`

## 本轮额外验证点

- 修正 `extract-prototype-outline.py` 的操作词误识别，避免把状态值或说明文字误判为真实按钮
- 修正 `shared/templates/需求总览模板.md` 的默认阶段口径，避免初始化即显示完成态
- 重新生成并复核 `原型解析摘要.md`、`需求文档.md`、`UI交互设计规范.md`

## 当前示例范围

- 原型解析：是
- 需求文档：是
- UI 交互文档：是
- Gate 验证：是
- 技术方案 / 开发 / 测试 / 发布：否

## 当前主要文件

- `00-需求总览.md`
- `需求文档.md`
- `UI交互设计规范.md`
- `manifest.json`
- `stage-status.json`
- `原型解析摘要.md`
