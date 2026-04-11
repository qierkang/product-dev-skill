---
name: product-dev-main
description: Use when 需要把原型 HTML、页面字段表、按钮说明或截图沉淀成需求文档，并按标准 Gate 推进到 UI 交互文档阶段。
---

# Product Dev Main

## 定位

这是 `product-dev-skill` 的统一业务入口，只负责把原型输入收敛成标准文档链路，不直接扩展成技术方案、开发任务或测试发布流程。

## 必读

1. `../../profiles/default/profile.yaml`
2. `../../shared/references/naming.md`
3. `../../shared/references/artifact-standard.md`
4. `../../shared/references/prototype-analysis.md`
5. `../../shared/references/requirement-gate.md`
6. `../../shared/references/ui-gate.md`
7. `../../shared/workflow/prototype-to-requirement.md`

## 标准动作

1. 先执行 `bash install/doctor.sh --capability docs`
2. 初始化 request：
   - `python3 shared/scripts/init-request.py --request-key <request-key> --workspace workspace/requests --title "<中文标题>"`
3. 把原型 HTML、截图或字段表整理到 `workspace/requests/<request-key>/assets/`
4. 执行原型解析脚本：
   - `python3 shared/scripts/extract-prototype-outline.py --request-dir workspace/requests/<request-key> --input <html-path>`
5. 先补 `00-需求总览.md`
6. 再补 `需求文档.md`
7. 执行 requirement Gate：
   - `python3 shared/scripts/stage-gate.py --request-dir workspace/requests/<request-key> --stage requirement`
8. 进入 UI 阶段时，继续调用：
   - `../../skills/product-dev-ui/SKILL.md`

## 当前固定产物

- `00-需求总览.md`
- `需求文档.md`
- `UI交互设计规范.md`
- `manifest.json`
- `stage-status.json`
- `原型解析摘要.md`（可选但建议保留）

## 关键约束

1. 需求文档模板默认继承 Picasso 版，不自行弱化字段来源、系统字段、表单定义和按钮逻辑。
2. 原型如果已标注 `主表 / 子表 / 孙表`，需求文档必须保留层级。
3. 原型中疑似模板残留、文案污染、状态枚举混杂时，不能直接当成有效规则写死，必须放进“待确认项”。
4. 先需求文档，后 UI 文档；不允许跳过 requirement Gate 直接写 UI。

## 不做

- 不产出技术方案
- 不拆开发任务
- 不进入开发、自测、审查、冒烟、验收、发布
- 不连接数据库
- 不启动前后端服务
