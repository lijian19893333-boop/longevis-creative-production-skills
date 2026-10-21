# 参与 Longevity Skills · LONGEVIS 项目

[English](CONTRIBUTING.md) | [Wiki](https://github.com/lijian19893333-boop/longevis-creative-production-skills/wiki) | [公开改进看板](https://github.com/users/lijian19893333-boop/projects/1)

欢迎分享从实际任务中得到的改进，包括更清楚的指令、通用示例、翻译、可复现的问题和小范围脚本修复。中文、英文都可以。

## 反馈问题或提出建议

先搜索已有 Issue，再[选择反馈表单](https://github.com/lijian19893333-boop/longevis-creative-production-skills/issues/new/choose)。问题报告请提供 Skill 名称、版本或提交、环境、最小输入、复现步骤、预期和实际结果。改进建议请说明真实任务，以及怎样判断改进有效。

## 提交改进

1. 较大改动先提 Issue 讨论范围；小修正可以直接提交 PR。
2. Fork 仓库并创建分支，一次集中解决一个问题。
3. 保持 `SKILL.md` 与 `SKILL.en.md` 完全一致；涉及含义变化时，同步更新 `SKILL.zh-CN.md` 及对应参考文档。安装名统一为 `longevity-*`，LONGEVIS 为维护品牌。
4. 输入、依赖或入口变化时，同步更新 `catalog.json`、示例和链接。
5. 运行下面的检查，在 PR 中说明结果；必要时提供小型合成示例，方便复现。

```sh
python -m pip install PyYAML==6.0.2
python .github/scripts/check_repository.py
python skills/longevity-product-appearance-calibration/scripts/test_apply_glb_recipe.py
```

GitHub Actions 会在 PR 和 main 分支提交时运行相同检查。这些检查覆盖包结构和部分辅助脚本行为；实际渲染、生产部署、硬件联调和正式申请仍需具体项目验证。请说明实际完成了哪些检查。

## 查看进展

公开看板分为 **Todo（待办）**、**In Progress（进行中）**、**Done（已完成）**。新建的开放 Issue 由看板的仓库导入流程加入。建议进入待办不等于交付承诺；开始前先在 Issue 中交流，避免重复工作，维护者会核对范围与验收证据后关闭任务。

请使用有权公开的示例，移除密钥、客户资料和未公开产品或发明细节。贡献内容应与仓库 [MIT License](LICENSE) 兼容，并保留外部来源及[第三方许可](THIRD_PARTY_NOTICES.md)。讨论请尊重他人，尽量具体。

公司与合作交流：[248234067@qq.com](mailto:248234067@qq.com)。
