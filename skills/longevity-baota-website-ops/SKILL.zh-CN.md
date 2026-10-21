---
name: longevity-baota-website-ops
description: Use when uploading, updating, publishing, migrating, or rolling back websites on Baota, self-hosted servers, Nginx, systemd, or PM2, including ambiguous static versus SSR artifacts or uncertain deployment status.
---

# Longevity · 宝塔与自托管网站发布

[English](SKILL.md)

把每次发布做成可验证、可恢复的版本切换。先发现项目实际构建与运行方式，再决定上传什么；面板登记、进程运行、内网健康、正式域名可用是不同证据。

## 开始前

记录目标站点、环境、域名、源码版本、构建脚本与产物、生产目录、运行入口、托管者、监听地址/端口、数据库/私有媒体/env/配置和回滚点。读取当前项目 README、包管理器锁文件、脚本和部署文档；不从本 skill 或旧记录猜路径、端口、Node 版本、命令或账号。

保留用户已授予的操作范围。用户授权发布且目标明确时，完成备份、候选版本验证后继续切换，不再重复索要同一授权。仅在关键目标不明、实际操作越出授权或工具要求审批时暂停依赖动作；仍可继续独立准备。skill 本身不授予生产操作权限。

## 发布判断

| 观察 | 决定 |
| --- | --- |
| 项目确认静态导出，构建输出含入口 HTML | 静态文件由 Nginx 提供；独立识别 API/后台服务 |
| 项目确认 SSR/Node 服务且存在匹配入口 | 按项目启动契约部署运行文件、依赖和服务；Nginx 反代 |
| 同时存在 `dist/`、`.output/` 等产物 | 查脚本、README 与实际生产入口，排除旧产物；不能凭文件夹猜 |
| 缺失预期产物或启动契约冲突 | 修复构建/配置后再发布 |

`dist/index.html` 和 `.output/server/index.mjs` 是常见例子，不是通用标准；其他框架产物以项目证据为准。

## 执行约束

1. 按最高影响面分级。文案/图片可走已存在的后台草稿与预览；涉及 API、数据库、env、权限、服务、域名或 DNS 时，处理完整应用及配置，不能只传前端。
2. 在本地或隔离构建环境执行项目实际存在的检查与构建。生成必要运行文件的发布包，核对清单、大小与 SHA-256；按运行契约保留必需依赖，不盲目排除所有依赖目录。
3. 保留旧版本，在独立候选目录/测试站验收。备份数据库、私有媒体、env 和 Nginx/服务配置，验证备份可读与恢复步骤；持久化数据放在版本目录和 Web 根目录之外。
4. 服务只由一个托管者负责。宝塔 Node、systemd 与 PM2 不得重复抢同一端口。迁移托管方式需覆盖 env、数据、进程、流量切换和回滚。
5. 候选版本通过后按既有授权切换；域名/DNS 变更仅在授权范围内实施。按实际影响验证正式 URL、关键业务流程与恢复路径。

部署、维护与回滚的详细步骤见[中文运行手册](references/deployment-runbook.zh.md)，英文对应见[English runbook](references/deployment-runbook.en.md)。

## 交付证据

报告源码版本、构建与包校验结果、候选验收、备份位置、实际服务托管者、正式 URL 验证、已知问题与回滚点。明确哪些仅本地/测试站通过，哪些已在正式环境核验。不得以“上传成功”“运行中”或“本地正常”宣称正式上线完成。

真实密码、Token、Cookie、SMTP 凭据、数据库和私有媒体不得进入聊天、Git、公开产物或脱敏前的日志。此公开版只提供方法，不包含任何站点凭据，也不证明某个站点已经上线。
