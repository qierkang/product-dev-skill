---
name: product-dev-maintainer
description: Use when 修改 product-dev-skill 自身的模板、脚本、README、规则或示例，并需要同步治理记录与示例验证。
---

# Product Dev Maintainer

## 适用场景

- 调整 `README.md`
- 调整 `SKILL.md` 与 companion skills
- 修改 `shared/templates/`
- 修改 `shared/scripts/`
- 更新 `profiles/`
- 追加或更新 `examples/`

## 必做动作

1. 更新 `governance/CHANGELOG.md`
2. 在 `governance/updates/` 增加本次变更记录
3. 结构性调整时，在 `governance/decisions/` 增加决策记录
4. 如果改了模板或 Gate，必须至少跑一遍真实模拟

## 维护边界

- 不保留失效的旧流程名
- 不让 README 和脚本行为互相矛盾
- 不让示例产物落后于模板当前版本
