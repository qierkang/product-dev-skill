# Workspace

运行时需求目录统一放在：

- `workspace/requests/<request-key>/`

临时模拟、陪跑记录可放：

- `workspace/simulations/`

约定：

- `workspace/` 只放运行期目录和临时过程产物，不作为正式示例交付目录
- 正式保留的可复用示例统一沉淀到 `examples/`
- `workspace/requests/` 与 `workspace/simulations/` 默认不提交到 Git
