# chg-0002 second-run recheck and parser hardening

## 时间

`2026-04-11`

## 结论

对同一组项目管理原型完成第二轮真实陪跑复验，并根据复验结果对摘要脚本和模板做了两项收口：

1. 收紧 `extract-prototype-outline.py` 的操作词识别规则，避免把状态值和说明文案误判为真实操作
2. 修正 `shared/templates/需求总览模板.md` 的默认阶段口径，避免新 request 初始化后直接显示完成态

## 背景

首轮陪跑已经跑通最小链路，但第二轮复核时发现两个容易误导使用者的问题：

- 原型解析摘要会把 `已取消` 之类状态值中的 `取消` 误判成按钮操作
- `00-需求总览.md` 模板默认把 `当前阶段` 写成了完成态，不符合真实初始化语义

这两个问题虽然不影响 Gate 通过，但会直接降低真实使用时的判断质量。

## 本次改动

- 脚本：
  - `shared/scripts/extract-prototype-outline.py`
    - 增加更严格的操作词匹配
    - 对 `查询条件` 这类说明文字增加过滤
- 模板：
  - `shared/templates/需求总览模板.md`
    - 默认阶段改为 `需求分析中`
- 示例：
  - 新增 `examples/project-management-pm-recheck/`
  - 第二轮 request 与 example 均通过 `requirement / ui / all`

## 验证

- `bash install/doctor.sh --capability docs`
- `python3 shared/scripts/init-request.py ...`
- `python3 shared/scripts/extract-prototype-outline.py ...`
- `python3 shared/scripts/stage-gate.py --stage requirement`
- `python3 shared/scripts/stage-gate.py --stage ui`
- `python3 shared/scripts/stage-gate.py --stage all`
- `python3 -m py_compile shared/scripts/*.py`
- `examples/project-management-pm-recheck` 再跑 `--stage all`

## 下一步

- 继续用其他业务原型验证操作词识别的泛化能力
- 如果后续再发现“按钮词被状态值误命中”的场景，优先继续在解析脚本层收口，而不是把噪音留给文档人工处理
