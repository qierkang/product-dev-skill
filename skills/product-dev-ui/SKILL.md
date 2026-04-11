---
name: product-dev-ui
description: Use when 产品需求已经形成文档基线，需要继续输出页面结构、交互路径、状态说明和验收要点的 UI 交互文档。
---

# Product Dev UI

## 定位

该 skill 专门负责 `UI交互设计规范.md`，输入必须是已经补齐过的 `需求文档.md` 和原型摘要，而不是直接跳过需求阶段从 HTML 生写 UI。

## 必读

1. `../../shared/templates/UI交互设计模板.md`
2. `../../shared/references/ui-gate.md`
3. `../../shared/references/prototype-analysis.md`
4. `../product-dev/SKILL.md`

## 标准动作

1. 先读 `00-需求总览.md`
2. 再读 `需求文档.md`
3. 复核 `原型解析摘要.md`
4. 产出 `UI交互设计规范.md`
5. 执行 UI Gate：
   - `python3 shared/scripts/stage-gate.py --request-dir workspace/requests/<request-key> --stage ui`

## 文档重点

- 页面分区
- 核心交互路径
- 表单校验与联动
- 状态与按钮显隐
- 空态 / 加载态 / 错误态
- 视觉与端差异说明
- 验收要点

## 关键约束

1. UI 文档必须以需求文档为准，不得和需求文档自相矛盾。
2. 所有按钮、弹窗、只读态、编辑态、查看态必须和原型一致；若不一致，写进“特殊说明”。
3. 不能只写视觉描述，必须写操作路径和状态规则。
