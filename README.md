# 乡村教师成长档案服务

Flask 后端把教师观察、授权和阶段成果存入 SQLite，数据库路径由 `DATABASE_PATH` 配置。迁移脚本在 `migrations`，当前入口可启动并返回健康状态。

运行：`python app.py`；测试：`python -m unittest`。
