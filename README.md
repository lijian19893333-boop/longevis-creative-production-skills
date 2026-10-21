# LONGEVIS 创作与产品交付 Skills

三个面向中文工作场景的 Agent Skill：科普视频、融资路演 BP、产品三维设计与画册渲染。

这些技能把内容核对、可编辑制作和交付验收连在一起。它们提供工作方法和部分辅助脚本，实际成品仍需要对应工具、项目素材与人工评审。

| Skill | 适用任务 | 附带内容 |
| --- | --- | --- |
| [longevis-science-video](skills/longevis-science-video/SKILL.md) | 科普脚本、机制动画、旁白字幕与视频验收 | 通用流程、brief 示例；不含渲染工程 |
| [longevis-roadshow-bp](skills/longevis-roadshow-bp/SKILL.md) | 新建或重做融资路演 BP | 商业叙事、配图规范、PPTX 图片审计脚本 |
| [longevis-product-3d-workflow](skills/longevis-product-3d-workflow/SKILL.md) | 产品建模迭代、方案同步、多视角渲染 | Blender 渲染、源文件快照、图片打包脚本与配置 |

## 安装到 Codex

将需要的单个 Skill 文件夹复制到你的 Codex skills 目录，常见位置为 `~/.codex/skills/`。先克隆仓库，再复制需要的技能：

```sh
git clone https://github.com/lijian19893333-boop/longevis-creative-production-skills.git
cd longevis-creative-production-skills
mkdir -p ~/.codex/skills
cp -R skills/longevis-roadshow-bp ~/.codex/skills/
```

复制前检查同名目录，已有版本时先备份，避免覆盖。重新打开会话后确认 Skill 已被识别。其他 Agent 环境请按其 Skill 安装方式复制对应目录。

## 使用示例

```text
使用 $longevis-science-video，制作一个解释声音如何传播的 60 秒科普视频。
先核验资料，生成可评审样片，并交付字幕和可编辑分镜。
```

```text
使用 $longevis-roadshow-bp，把我提供的项目资料整理成 12 页融资路演 BP。
保留关键事实，未知数据用可编辑填写位，融资放在最后。
```

```text
使用 $longevis-product-3d-workflow，基于我的参考图和尺寸建立 A/B 两套产品方案。
保留源模型，先试渲染，再输出正式 PNG、JPG 和总览。
```

## 运行依赖与边界

- 科普视频：按制作方案准备 Remotion / Three.js、Blender、FFmpeg 或配音工具。本仓库不提供完整渲染器，也不绑定付费服务。
- 路演 BP：需要可编辑 PPTX 制作与渲染工具。`audit_pptx.py` 使用 Python 标准库，只能检查字节级图片复用、缺失引用等，不能替代视觉验收。
- 产品三维：普通脚本需要 Python 3.10+；渲染脚本在 Blender Python 中运行；图片打包需要 Pillow 及覆盖标签文字的字体。示例中的尺寸、机位、对象名和路径必须适配实际模型。
- 所有示例是工作流演示，不构成已确认项目数据、工程制造结论、产品疗效或融资承诺。

## 公开版处理

公开版移除了本机项目路径、私人配音历史、真实项目案例图和专属参数说明。原始模型、影片工程、客户资料与商业演示稿未包含在本仓库中。

## 许可

本仓库全部 Skill 文档、脚本与示例以 [MIT License](LICENSE) 开源。允许使用、修改、再分发和商业使用，须保留版权与许可声明。外部工具、模型、素材与服务适用各自许可，不随本仓库授权。
