# LONGEVIS 创作与产品交付 Skills

[English](README.md) | **简体中文** | [Wiki：公司介绍与使用指南](https://github.com/lijian19893333-boop/longevis-creative-production-skills/wiki)

十个从 [LONGEVIS 朗静岛](https://www.longevis.net/) 日常工作中总结出来的开源 AI Agent Skill。我们自己使用，也在实际项目中不断调整和完善，希望这些经验能帮助到有相似需求的人。

每个 Skill 都有完整中英文指令和对应语言的 Markdown 参考文档；脚本与机器可读配置共享使用。按任务选一个安装即可。

## 关于 LONGEVIS 朗静岛

LONGEVIS 朗静岛是一家面向 biohacking（生物黑客）与 longevity（长寿健康）领域的硬件解决方案公司，提供恢复科技设备与空间整体配置方案。产品覆盖纯电冷冻舱、液氮冷冻舱、微高压氧舱、红外光能舱和干式漂浮床。我们的工作从实体产品延伸到产品设计、数字交互、科普内容、网站和项目交付。

这些 Skill 就来自这些日常工作。研发和交付设备的同时，我们需要根据参考图建立三维模型、校准材质和光感、用视频解释技术原理、准备演示资料、梳理控制屏交互、整理工程文档，以及上线和维护网站。

更多公司与产品信息，请访问 [LONGEVIS 朗静岛官网](https://www.longevis.net/)。合作、公司及 Skill 相关交流，欢迎联系 **[248234067@qq.com](mailto:248234067@qq.com)**；可复现的 Skill 问题与改进建议，请提交到 [GitHub Issues](https://github.com/lijian19893333-boop/longevis-creative-production-skills/issues)。

## 从日常工作中总结，再分享给大家

我们先从自己手头真正要完成的任务出发，在使用 AI Agent 的过程中不断调整指令，记录反复遇到的问题，梳理出完成任务所需的步骤和验收方法，再把这些经验整理成可复用的 Skill，根据需要配上参考文档、模板或辅助脚本。

这个过程可以概括为：**实际工作需求 → 日常使用与迭代 → 总结经验 → 提炼通用方法 → 开源分享**。

这些 Skill 记录了我们目前积累的工作方法。希望它们能帮其他开发者、设计师和团队推进自己的项目，也欢迎大家结合不同场景补充和改进。

## Skill 目录

| 中文入口 | English | 用途 |
|---|---|---|
| [科普视频](skills/longevis-science-video/SKILL.zh-CN.md) | [English](skills/longevis-science-video/SKILL.md) | 资料、机制分镜、旁白字幕与媒体验收 |
| [融资路演 BP](skills/longevis-roadshow-bp/SKILL.zh-CN.md) | [English](skills/longevis-roadshow-bp/SKILL.md) | 叙事、证据、可编辑页面与 PPTX 图片审计 |
| [产品三维与画册渲染](skills/longevis-product-3d-workflow/SKILL.zh-CN.md) | [English](skills/longevis-product-3d-workflow/SKILL.md) | A/B 方案、模型快照、批量渲染与图片打包 |
| [网站上线与维护](skills/longevis-website-launch/SKILL.zh-CN.md) | [English](skills/longevis-website-launch/SKILL.md) | 媒体、域名/HTTPS、上线和 SEO/GEO 验收 |
| [看图建模](skills/longevis-reference-product-modeling/SKILL.zh-CN.md) | [English](skills/longevis-reference-product-modeling/SKILL.md) | 多视图几何校准、轮廓比对、真实模型与本地查看器 |
| [材质与光感校准](skills/longevis-product-appearance-calibration/SKILL.zh-CN.md) | [English](skills/longevis-product-appearance-calibration/SKILL.md) | 材质、光照、GLB 配方与原生/网页显示核对 |
| [宝塔部署与回滚](skills/longevis-baota-website-ops/SKILL.zh-CN.md) | [English](skills/longevis-baota-website-ops/SKILL.md) | 静态/SSR 识别、持久数据、候选版本与公开验证 |
| [外观设计六视图](skills/longevis-design-patent-3d-workflow/SKILL.zh-CN.md) | [English](skills/longevis-design-patent-3d-workflow/SKILL.md) | 原生模型、六向方向、完整轮廓与图包一致性 |
| [设备控制屏与 APP](skills/longevis-chamber-app/SKILL.zh-CN.md) | [English](skills/longevis-chamber-app/SKILL.md) | 功能、设置、状态机、ACK/真实反馈与验收规范 |
| [技术交底与工程附图](skills/longevis-patent-drafting/SKILL.zh-CN.md) | [English](skills/longevis-patent-drafting/SKILL.md) | 事实、部件、文稿、标注与可编辑图源一致性 |

## 安装

先克隆仓库，将需要的单个文件夹复制到所用 Agent 的技能目录。Codex 常见位置是 `~/.codex/skills/`：

```sh
git clone https://github.com/lijian19893333-boop/longevis-creative-production-skills.git
cd longevis-creative-production-skills
mkdir -p ~/.codex/skills
cp -R skills/longevis-reference-product-modeling ~/.codex/skills/
```

复制前检查并备份同名目录。新会话中确认技能被识别。`SKILL.md` 为默认英文指令；完整中文版本在同目录的 `SKILL.zh-CN.md`。旧 `SKILL.en.md` 英文链接继续可用。输出语言按用户要求，未指定时沿用对话语言；其他 Agent 按其安装约定操作。

## 调用示例

```text
使用 $longevis-reference-product-modeling，根据参考图与已确认尺寸建立可编辑模型。
先核对轮廓和视图关系，交付原生文件、GLB、查看器与仍存在的差异。
```

```text
使用 $longevis-chamber-app，审阅当前控制屏的设置保存与掉线恢复。
区分需求、源码、模拟、通信和实机验证，不连接或驱动设备。
```

```text
使用 $longevis-baota-website-ops，检查网站发布候选和回滚方案。
从实际工程发现构建/启动入口，在已有授权范围内完成对应工作。
```

## 工具、证据和公开范围

工作方法不等于工具安装、生产代码或成品生成器。视频仍需制作工程与音频工具，PPT 需可编辑制作用具，三维需原生模型工具，部署需实际项目和托管访问。详见英文依赖表及各 Skill 的说明。

公开版不含客户资料、真实产品模型、未公开发明、配方、内部控制协议、生产参数、服务器配置、账号或密钥。设备和专利 Skill 提供通用方法及空表；不表示某种产品已安全验证、某件申请已递交或获批。外部素材的许可需另行核对。

本次检查覆盖结构、链接、隐私模式、双语内容、部分合成脚本测试和场景评审。实际视频、产品渲染、生产部署、硬件联调和正式申请均须按具体项目验证。查看 [版本与验证范围](CHANGELOG.md) 和 [第三方许可](THIRD_PARTY_NOTICES.md)。

## 许可与参与

本仓库自有文档、辅助脚本与示例采用 [MIT License](LICENSE)。查看器内第三方代码保留各自版权与许可，不转授品牌标志或外部项目资产权利。欢迎在 Issues 提交可复现问题，在 PR 中说明目的、输入、实际检查和依赖。
