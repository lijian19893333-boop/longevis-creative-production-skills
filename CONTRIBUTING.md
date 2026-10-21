# Contributing to Longevity Skills by LONGEVIS

[简体中文](CONTRIBUTING.zh-CN.md) | [Wiki](https://github.com/lijian19893333-boop/longevis-creative-production-skills/wiki) | [Public roadmap](https://github.com/users/lijian19893333-boop/projects/1)

We welcome improvements based on real tasks: clearer instructions, reusable examples, translations, reproducible bug reports and focused helper fixes. English and Chinese are both welcome.

## Report or propose

Search existing issues first, then [choose a feedback form](https://github.com/lijian19893333-boop/longevis-creative-production-skills/issues/new/choose). Bugs should include the skill name, version or commit, environment, minimal inputs, steps, expected result and actual result. Proposals should explain the real task and how a useful improvement can be checked.

## Make a contribution

1. For substantial changes, discuss scope in an issue before building. For small fixes, a direct pull request is fine.
2. Fork the repository, create a branch and keep the change focused on one problem.
3. Keep `SKILL.md` and `SKILL.en.md` identical; update `SKILL.zh-CN.md` and corresponding reference documents when meaning changes. Installable names use `longevity-*`; LONGEVIS is the maintaining brand.
4. Update `catalog.json`, examples and links if inputs, dependencies or entrypoints change.
5. Run the checks below and describe the results in the pull request. Share a small synthetic example when it helps reproduce the change.

```sh
python -m pip install PyYAML==6.0.2
python .github/scripts/check_repository.py
python skills/longevity-product-appearance-calibration/scripts/test_apply_glb_recipe.py
```

GitHub Actions runs the same checks for pull requests and main-branch pushes. It checks package structure and helper behavior; actual rendering, production deployment, hardware integration and filing still need project-specific validation. State clearly which of those checks you performed.

## Follow the work

The public board uses **Todo**, **In Progress** and **Done**. Open issues are added to the board by its repository import workflow. A proposal is not a delivery commitment. Discuss an issue before starting work to avoid duplication; maintainers review scope and acceptance evidence before closing it.

Use examples you have permission to publish. Remove credentials, customer information and unpublished product or invention details. Contributions should be compatible with the repository's [MIT License](LICENSE); preserve external attribution and [third-party notices](THIRD_PARTY_NOTICES.md). Keep feedback respectful and specific.

Company and collaboration enquiries: [248234067@qq.com](mailto:248234067@qq.com).
