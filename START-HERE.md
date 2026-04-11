# START HERE

第一次使用 `product-dev-skill`，按这份顺序进入。

## 先做什么

1. 阅读 `README.md`
2. 阅读 `SKILL.md`
3. 阅读 `skills/product-dev/SKILL.md`
4. 阅读 `profiles/default/profile.yaml`
5. 执行 `doctor docs`

## 当前包只做什么

- 读原型 HTML / 截图 / 字段表
- 生成 `需求文档.md`
- 基于需求文档生成 `UI交互设计规范.md`
- 用 Gate 检查文档是否达到最小交付标准

## 当前包不做什么

- 不负责技术方案、开发、测试、上线
- 不连接数据库
- 不启动前后端服务
- 不进入 `test / uat / prod`

## 最小执行命令

```bash
bash install/setup.sh
bash install/doctor.sh --capability docs
python3 shared/scripts/init-request.py --request-key demo --workspace workspace/requests --title "示例需求"
```
