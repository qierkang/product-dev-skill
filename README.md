# Product Dev Skill

<!-- Keywords: product requirements skill, prototype analysis, UI interaction specification, Claude Code skill, Codex skill, HTML prototype to PRD, stage gate -->

<div align="center">
  <img src="./assets/social-preview.png?v=1" alt="Product Dev Skill social preview" width="100%">
</div>

<div align="center">
  <strong>把 HTML 原型、截图、字段表和页面说明转成结构化需求文档与 UI 交互规范</strong>
  <br><br>
  <em>统一输入、模板、阶段状态与 Gate，让不同产品经理和不同 AI 运行端得到同一套文档基线。</em>
  <br><br>
  <code>SKILL.md</code> · Prototype Analysis · Requirements · UI Spec · Stage Gate
  <br><br>
  从原型输入，到可开发、可验收、可回放的产品文档。
  <br><br>
  如果这个项目节省了你的产品整理时间，公开发布后欢迎点亮一颗 Star。
</div>

<div align="center">
  <a href="#快速开始">快速开始</a> ·
  <a href="./docs/README_en.md">English</a> ·
  <a href="#工作流总览">工作流</a> ·
  <a href="#系统架构">架构</a> ·
  <a href="#常见问题">FAQ</a>
</div>

<div align="center">

![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Version](https://img.shields.io/badge/version-0.2.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![Scope](https://img.shields.io/badge/scope-prototype%20to%20UI%20spec-orange?style=for-the-badge)
![Runtime](https://img.shields.io/badge/runtime-multi--agent-111827?style=for-the-badge)
![PRs](https://img.shields.io/badge/PRs-welcome-2563eb?style=for-the-badge)
[![CI](https://github.com/qierkang/product-dev-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/qierkang/product-dev-skill/actions/workflows/ci.yml)
[![Stars](https://img.shields.io/github/stars/qierkang/product-dev-skill?style=for-the-badge)](https://github.com/qierkang/product-dev-skill/stargazers)

</div>

---

![Product Dev Skill 中文工作流架构](./assets/platform/architecture/zh-CN/product-dev-skill-architecture.png)

---

## 为什么需要 Product Dev Skill？

- 原型页面只表达视觉结果，字段、权限、规则、异常和回写逻辑经常缺失。
- 产品经理使用不同模型和提示词时，需求文档结构与颗粒度不稳定。
- 主表、子表、孙表层级容易在口语化整理中被合并或丢失。
- UI 交互文档如果没有状态、边界和验收条件，开发仍需二次猜测。
- 没有阶段状态和 Gate 时，文档看似完成，实际仍存在关键空洞。

**Product Dev Skill 把原型识别、需求建模、UI 规范和阶段校验变成一条最小但完整的交付链。**

```text
使用 product-dev，把这组 HTML 原型整理成需求文档和 UI 交互设计规范。
```

| 临时整理 | 本项目 |
|---|---|
| 页面截图逐段描述 | 识别页面、组件、字段、关系与规则 |
| 文档结构因人而异 | 使用稳定模板和命名约定 |
| 需求与 UI 文档脱节 | 两个主产物按同一 request 状态推进 |
| 完成标准靠主观判断 | requirement / ui / all 三类 Gate |
| 结果难以复盘 | manifest、stage-status、logs 可回放 |

## 项目概述

Product Dev Skill 是一个专注产品原型文档化的自包含技能包。它读取原型 HTML、截图、字段表和页面说明，先生成结构化需求文档，再生成 UI 交互设计规范，并通过阶段 Gate 检查完整性、一致性与必需产物。它不负责编码、联调、测试和发布，适合产品团队稳定完成开发前的需求与设计交接。

> Product Dev Skill turns prototypes into structured requirements and UI interaction specifications with repeatable templates and stage gates.
>
> If this saves you time, a ⭐ helps others find it.

## 核心特色

- **原型结构化建模**：识别页面、区域、组件、字段、按钮、表格和业务关系。
- **双主产物闭环**：固定产出 `需求文档.md` 与 `UI交互设计规范.md`。
- **强模板约束**：保留主/子/孙表层级、边界条件、状态和验收口径。
- **阶段 Gate**：用 `stage-gate.py` 检查 requirements、UI 与全流程完整性。
- **设计能力可插拔**：优先协同 `ui-ux-pro-max`，缺失时回退到内置设计规则。

## 与同类方案对比

| 方案 | 原型解析 | 结构化需求 | UI 交互规范 | 阶段 Gate | 可回放 |
|---|---:|---:|---:|---:|---:|
| **Product Dev Skill** | ✅ | ✅ | ✅ | ✅ | ✅ |
| 通用文档提示词 | 部分 | 不稳定 | 部分 | ❌ | ❌ |
| 原型导出工具 | ✅ | 视觉为主 | 部分 | ❌ | 部分 |
| 完整研发流程 skill | ✅ | ✅ | ✅ | ✅ | ✅，但范围更重 |

## 工作流总览

| 阶段 | 动作 | 输出 |
|---|---|---|
| 环境检查 | `doctor.sh --capability docs` | 可执行环境 |
| request 初始化 | `init-request.py` | 目录、manifest、stage status |
| 原型抽取 | `extract-prototype-outline.py` | 原型解析摘要 |
| 需求建模 | 按模板补业务、字段、规则、边界 | `需求文档.md` |
| Requirement Gate | 完整性与规则检查 | requirements pass/fail |
| UI 规范 | 补布局、组件、状态、交互、端差异 | `UI交互设计规范.md` |
| UI / All Gate | 一致性与最终检查 | 可交付 request |

不确定从哪里开始时，先运行 doctor，再从 `product-dev` 主入口进入。

## 快速开始

### 前置条件

- Python 3。
- 支持读取 `SKILL.md` 的运行端。
- 原型 HTML、截图、字段表或页面说明中的至少一种。

```bash
git clone https://github.com/qierkang/product-dev-skill.git
cd product-dev-skill
bash install/setup.sh
bash install/doctor.sh --capability docs
```

```bash
python3 shared/scripts/init-request.py \
  --request-key project-management-demo \
  --workspace workspace/requests \
  --title "项目管理"

python3 shared/scripts/extract-prototype-outline.py \
  --request-dir workspace/requests/project-management-demo \
  --input /path/to/page-a.html \
  --input /path/to/page-b.html
```

<details>
<summary>查看标准产物</summary>

```text
workspace/requests/<request-key>/
├── 00-需求总览.md
├── 需求文档.md
├── UI交互设计规范.md
├── 原型解析摘要.md
├── manifest.json
├── stage-status.json
├── assets/
└── logs/
```

</details>

## 功能模块

### `product-dev`

- 初始化 request 和机器可读状态。
- 识别原型输入类型并加载模板、规则与 profile。
- 组织需求文档生成和 requirement Gate。

### `product-dev-ui`

- 将需求规则映射到页面、组件、状态和交互。
- 记录空态、加载态、异常态与权限差异。
- 输出可用于开发和 UI 验收的交互规范。

### `product-dev-methods`

- 提供原型分析、最小上下文加载和阶段自检方法。
- 保留业务边界、技术边界与权限边界。
- 记录风险、异常处理和回退策略。

### `product-dev-maintainer`

- 维护模板、规则、脚本、版本和治理记录。
- 确保示例与 Gate 同步更新。
- 管理多运行端适配说明。

## 技术栈

| 层级 | 技术或资产 | 说明 |
|---|---|---|
| 技能入口 | `SKILL.md` | 主流程与 companion 路由 |
| 原型解析 | Python | HTML 结构、语义和关系抽取 |
| 文档模板 | Markdown | 需求与 UI 交互基线 |
| 状态管理 | JSON | manifest 与 stage status |
| 阶段门禁 | `stage-gate.py` | 完整性、一致性、命名校验 |
| 配置 | YAML / `.env` | profile 与可迁移环境差异 |
| 视觉资产 | `image_gen` | README 架构和品牌图 |

## 系统架构

### 工作流设计

```text
Prototype HTML / screenshots / field tables
  -> product-dev
     -> identify pages, components, fields, relations, rules
     -> initialize request + stage state
     -> requirements document -> requirement gate
     -> UI interaction specification -> UI gate
     -> all gate -> replayable example
  -> product-dev-methods / product-dev-ui / maintainer
```

### 架构说明

- 主流程层只覆盖原型到需求/UI 文档，不进入编码和发布。
- 模板、规则和示例位于仓库内，避免运行端之间的提示词漂移。
- request 产物进入 `workspace/`，验证通过后才能选取脱敏示例进入 `examples/`。

![Product Dev Skill 资源架构](./assets/platform/architecture/zh-CN/product-dev-skill-architecture.png)

## 目录结构

```text
├── SKILL.md
├── skills/{product-dev,product-dev-ui,product-dev-methods,product-dev-maintainer}/
├── profiles/default/
├── shared/{templates,references,workflow,scripts}/
├── install/
├── examples/
├── governance/
├── assets/
├── docs/
└── workspace/requests/
```

## 命令参考

| 命令 | 说明 |
|---|---|
| `bash install/setup.sh` | 初始化目录 |
| `bash install/doctor.sh --capability docs` | 检查文档工作流环境 |
| `python3 shared/scripts/init-request.py ...` | 创建 request |
| `python3 shared/scripts/extract-prototype-outline.py ...` | 抽取原型摘要 |
| `python3 shared/scripts/stage-gate.py --request-dir <dir> --stage requirement` | 校验需求文档 |
| `python3 shared/scripts/stage-gate.py --request-dir <dir> --stage ui` | 校验 UI 文档 |
| `python3 shared/scripts/stage-gate.py --request-dir <dir> --stage all` | 校验完整 request |

## 开发指南

### 模板修改

以 `shared/templates/需求文档模板.md` 为核心基线，修改后同步示例与 Gate。

### 原型解析

解析器只生成结构化摘要，不应凭空补业务规则；不确定项进入待确认列表。

### 安全边界

- 不提交真实客户原型、截图和运行日志。
- 不在文档或脚本中写死个人宿主机路径。
- 不把主/子/孙表层级合并成扁平字段列表。

## 开发与验证

```bash
bash install/doctor.sh --capability docs
python3 shared/scripts/stage-gate.py \
  --request-dir examples/project-management-pm-recheck \
  --stage all
python3 scripts/readme-gate.py --readme README.md
python3 scripts/readme-gate.py --readme docs/README_en.md
```

doctor 无 `FAIL`、示例 Gate 通过、README 与资产检查退出 `0` 才算验证通过。

## 项目状态

| 项目 | 当前值 |
|---|---|
| 版本 | `0.2.0` |
| 状态 | Active |
| 范围 | 原型分析 → 需求文档 → UI 交互文档 → Gate |
| 运行端 | Claude Code / Codex / OpenClaw / OpenCode |
| 已知边界 | 不覆盖编码、联调、QA 和发布 |

## 常见问题

<details>
<summary>这个 skill 会直接开发代码吗？</summary>

不会。它的完成边界是需求文档与 UI 交互规范通过 Gate。
</details>

<details>
<summary>只有截图，没有 HTML 可以使用吗？</summary>

可以，但字段类型、校验规则和业务关系需要额外说明或进入待确认项。
</details>

<details>
<summary>没有 ui-ux-pro-max 会中断吗？</summary>

不会。流程会回退到 `shared/references/design/`，且不会默认改用其他通用设计 skill。
</details>

<details>
<summary>何时可以把 request 放进 examples？</summary>

仅在 `stage-gate.py --stage all` 通过并完成脱敏后。
</details>

## 参与贡献

- Issue 请附输入类型、目标文档和 Gate 失败信息。
- 修改模板时同步更新示例和验证。
- 修改解析脚本时补最小复现输入。
- PR 前执行 doctor、示例 Gate、README 和资产校验。

详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。English contributors can use [docs/README_en.md](./docs/README_en.md).

## 版本说明

| 版本 | 主要变化 |
|---|---|
| `0.2.0` | 加入内置设计兜底与 UI Gate 强约束 |
| `0.1.0` | 初始化原型到需求/UI 文档最小链路 |

完整记录见 [CHANGELOG.md](./CHANGELOG.md) 与 [governance/CHANGELOG.md](./governance/CHANGELOG.md)。

## 致谢

本项目继承了 Picasso 文档模板与 Product Delivery 的轻量 Gate 思路，并通过真实原型复验持续收敛。

## Star History · Star 历史

公开仓库首次发布后，将通过 `platform-project-skill/scripts/add-star-history.sh` 写入真实图表。

<!-- star-history:start -->
Star History will be added after the first public push.
<!-- star-history:end -->

## 许可证

本项目采用 [MIT License](./LICENSE)。

## 作者

- Email: `xyqierkang@gmail.com`
- GitHub: [qierkang](https://github.com/qierkang)
