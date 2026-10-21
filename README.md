# LONGEVIS 创作与产品交付 Skills

**简体中文** | [English](README.en.md)

十个来自实际创作、产品交付和网站维护工作的 Agent Skill。每个 Skill 都有完整中文与英文入口，所需的 Markdown 参考文档提供对应语言版本；脚本和机器可读配置共享使用。按任务选一个安装即可。

本次新增六项：看图建模、材质与光感校准、宝塔部署、外观六视图、设备控制屏、技术交底与工程附图。原有四项同步补齐英文正文与参考文档。

| 中文入口 | English | 用途 |
|---|---|---|
| [科普视频](skills/longevis-science-video/SKILL.md) | [English](skills/longevis-science-video/SKILL.en.md) | 资料、机制分镜、旁白字幕与媒体验收 |
| [融资路演 BP](skills/longevis-roadshow-bp/SKILL.md) | [English](skills/longevis-roadshow-bp/SKILL.en.md) | 叙事、证据、可编辑页面与 PPTX 图片审计 |
| [产品三维与画册渲染](skills/longevis-product-3d-workflow/SKILL.md) | [English](skills/longevis-product-3d-workflow/SKILL.en.md) | A/B 方案、模型快照、批量渲染与图片打包 |
| [网站上线与维护](skills/longevis-website-launch/SKILL.md) | [English](skills/longevis-website-launch/SKILL.en.md) | 媒体、域名/HTTPS、上线和 SEO/GEO 验收 |
| [看图建模](skills/longevis-reference-product-modeling/SKILL.md) | [English](skills/longevis-reference-product-modeling/SKILL.en.md) | 多视图几何校准、轮廓比对、真实模型与本地查看器 |
| [材质与光感校准](skills/longevis-product-appearance-calibration/SKILL.md) | [English](skills/longevis-product-appearance-calibration/SKILL.en.md) | 材质、光照、GLB 配方与原生/网页显示核对 |
| [宝塔部署与回滚](skills/longevis-baota-website-ops/SKILL.md) | [English](skills/longevis-baota-website-ops/SKILL.en.md) | 静态/SSR 识别、持久数据、候选版本与公开验证 |
| [外观设计六视图](skills/longevis-design-patent-3d-workflow/SKILL.md) | [English](skills/longevis-design-patent-3d-workflow/SKILL.en.md) | 原生模型、六向方向、完整轮廓与图包一致性 |
| [设备控制屏与 APP](skills/longevis-chamber-app/SKILL.md) | [English](skills/longevis-chamber-app/SKILL.en.md) | 功能、设置、状态机、ACK/真实反馈与验收规范 |
| [技术交底与工程附图](skills/longevis-patent-drafting/SKILL.md) | [English](skills/longevis-patent-drafting/SKILL.en.md) | 事实、部件、文稿、标注与可编辑图源一致性 |

## 安装

先克隆仓库，将需要的单个文件夹复制到所用 Agent 的技能目录。Codex 常见位置是 `~/.codex/skills/`：

```sh
git clone https://github.com/lijian19893333-boop/longevis-creative-production-skills.git
cd longevis-creative-production-skills
mkdir -p ~/.codex/skills
cp -R skills/longevis-reference-product-modeling ~/.codex/skills/
```

复制前检查并备份同名目录。新会话中确认技能被识别。`SKILL.md` 为默认中文入口；需要完整英文指令时指定同目录的 `SKILL.en.md`。两者使用同一调用名；其他 Agent 按其安装约定操作。

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
