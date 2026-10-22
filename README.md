# Longevity Skills by LONGEVIS

**English** | [简体中文](README.zh-CN.md) | [Wiki: about us & getting started](https://github.com/lijian19893333-boop/longevis-creative-production-skills/wiki)

**Open-source Codex and AI agent workflows for Blender 3D modeling, GLB materials, science videos, investor pitch decks, HMI specifications, engineering figures, software copyright materials and website deployment.**

Eleven open-source AI agent skills distilled from the everyday work of [LONGEVIS](https://www.longevis.net/), a biohacking and longevity hardware solutions company. We use and refine these workflows in our own projects, and share them in the hope that they can help others with similar work.

Every skill has complete English and Chinese instructions and corresponding Markdown references. Executable helpers and machine-readable configurations are shared. Install only the skill needed for your task.

## About LONGEVIS

LONGEVIS (朗静岛) develops hardware and integrated equipment solutions for biohacking, longevity and recovery spaces. Our product range includes electric and nitrogen cryotherapy chambers, mild hyperbaric oxygen chambers, infrared wellness cabins and dry flotation beds. Our work connects physical products with their design, digital interfaces, educational content, websites and project delivery.

That work is where these skills come from. Alongside developing and delivering equipment, we need to model products from references, make materials and lighting consistent, explain technical principles in videos, prepare presentations, define control interfaces, organize engineering documents and maintain websites.

Learn more at the [LONGEVIS official website](https://www.longevis.net/). For collaboration or questions about LONGEVIS and these skills, contact **[248234067@qq.com](mailto:248234067@qq.com)**. For reproducible skill issues and improvement suggestions, please use [GitHub Issues](https://github.com/lijian19893333-boop/longevis-creative-production-skills/issues).

## From everyday work to reusable skills

We start with a task that needs doing in our own work. As we use AI agents to complete it, we refine the instructions, record recurring problems and identify the steps and checks that make the result useful. We then extract those lessons into a reusable skill, with supporting references, templates or helper scripts where needed.

The process is simple: **real work → daily use and iteration → lessons learned → reusable workflows → open source**.

These skills reflect what we have learned so far. We hope they help other builders, designers and teams make progress on their own projects, and we welcome improvements from people using them in different contexts.

## Skill catalog

| English entry | 中文 | Purpose |
|---|---|---|
| [Science videos](skills/longevity-science-video/SKILL.md) | [中文](skills/longevity-science-video/SKILL.zh-CN.md) | Sources, mechanism storyboards, narration, subtitles and media checks |
| [Investor pitch decks](skills/longevity-roadshow-bp/SKILL.md) | [中文](skills/longevity-roadshow-bp/SKILL.zh-CN.md) | Narrative, evidence, editable slides and PPTX image auditing |
| [Product 3D and brochure renders](skills/longevity-product-3d-workflow/SKILL.md) | [中文](skills/longevity-product-3d-workflow/SKILL.zh-CN.md) | A/B variants, source snapshots, batch rendering and image packaging |
| [Website launch](skills/longevity-website-launch/SKILL.md) | [中文](skills/longevity-website-launch/SKILL.zh-CN.md) | Media, domains/HTTPS, releases and SEO/GEO readiness |
| [Reference-based product modeling](skills/longevity-reference-product-modeling/SKILL.md) | [中文](skills/longevity-reference-product-modeling/SKILL.zh-CN.md) | Multi-view geometry, silhouette comparison, native models and a local viewer |
| [Material and lighting calibration](skills/longevity-product-appearance-calibration/SKILL.md) | [中文](skills/longevity-product-appearance-calibration/SKILL.zh-CN.md) | Materials, lighting, GLB recipes and native/browser display checks |
| [Baota deployment and rollback](skills/longevity-baota-website-ops/SKILL.md) | [中文](skills/longevity-baota-website-ops/SKILL.zh-CN.md) | Static/SSR routing, persistent data, release candidates and public verification |
| [Exterior design views](skills/longevity-design-patent-3d-workflow/SKILL.md) | [中文](skills/longevity-design-patent-3d-workflow/SKILL.zh-CN.md) | Native models, six-view orientation, complete silhouettes and package consistency |
| [Equipment control apps](skills/longevity-chamber-app/SKILL.md) | [中文](skills/longevity-chamber-app/SKILL.zh-CN.md) | Features, settings, state machines, ACK/physical feedback and acceptance specs |
| [Technical disclosures and engineering figures](skills/longevity-patent-drafting/SKILL.md) | [中文](skills/longevity-patent-drafting/SKILL.zh-CN.md) | Facts, components, drafts, annotation and editable figure-source consistency |
| [Software copyright applications and drafting](skills/longevity-software-copyright/SKILL.md) | [中文](skills/longevity-software-copyright/SKILL.zh-CN.md) | Agency templates, intake, function narratives, source provenance and drafter handoffs |

## Contribute and migrate

English and Chinese contributions are welcome. [Report an issue or suggest an improvement](https://github.com/lijian19893333-boop/longevis-creative-production-skills/issues/new/choose), read the [contribution guide](CONTRIBUTING.md), and follow the [public roadmap](https://github.com/users/lijian19893333-boop/projects/1). Pull requests run catalog, bilingual entrypoint, local-link, JSON/YAML and Python syntax checks, plus the GLB and software-copyright helper tests.

Since v0.4.0, all ten installation names use `longevity-*` in place of `longevis-*`. Back up local edits, install the new folder, confirm the new name in a fresh session, then remove the old folder to avoid duplicate loading. Previous versions remain in Git history. The repository URL is unchanged; LONGEVIS is the maintaining brand.

## Install

Clone the repository and copy an individual skill folder into your agent's skills directory. A common Codex location is `~/.codex/skills/`:

```sh
git clone https://github.com/lijian19893333-boop/longevis-creative-production-skills.git
cd longevis-creative-production-skills
mkdir -p ~/.codex/skills
cp -R skills/longevity-reference-product-modeling ~/.codex/skills/
```

Check for and back up an existing folder before copying. Confirm recognition in a new session. `SKILL.md` is the default English instruction file. Full Chinese instructions are in `SKILL.zh-CN.md` in the same folder. Existing `SKILL.en.md` links remain available. Follow the user’s requested output language, or their conversation language when unspecified. Follow the corresponding installation conventions in other agents.

## Example prompts

```text
Use $longevity-reference-product-modeling.
Create an editable model from my references and confirmed dimensions.
Check silhouettes and view relationships first; deliver native files, GLB,
a viewer and remaining differences.
```

```text
Use $longevity-chamber-app to review settings persistence and reconnection.
Separate requirements, source evidence, simulation, communication and hardware tests.
Do not connect to or operate equipment.
```

```text
Use $longevity-baota-website-ops to inspect my release candidate and rollback plan.
Discover actual build/start entrypoints and work within the authorization already given.
```

```text
Use $longevity-software-copyright to compare our package with the drafter's template.
Prepare editable materials, verify source scope and list remaining gaps per software.
```

## Dependencies

| Skill | Tools or project access |
|---|---|
| `longevity-science-video` | Remotion / Blender / FFmpeg / narration tools as selected; no full renderer bundled |
| `longevity-roadshow-bp` | Editable presentation authoring/rendering tools; audit helper uses Python standard library |
| `longevity-product-3d-workflow` | Python 3.10+, Blender; Pillow and suitable fonts for image packaging |
| `longevity-website-launch` | Actual project and authorized hosting access; commands discovered from the project |
| `longevity-reference-product-modeling` | Blender; Python + Pillow for masks; local HTTP server and WebGL-capable browser |
| `longevity-product-appearance-calibration` | Python standard library for helper; 3D renderer/browser for visual acceptance |
| `longevity-baota-website-ops` | Authorized host/project access; actual Nginx and process-manager environment |
| `longevity-design-patent-3d-workflow` | Native 3D tool, image inspection; current filing requirements verified per task |
| `longevity-chamber-app` | Current project evidence; no controller implementation or production protocol bundled |
| `longevity-patent-drafting` | Current evidence, appropriate CAD/3D/document tools; no private inventions bundled |
| `longevity-software-copyright` | Python 3.10+ standard library for helpers; actual source, current requirements and Word/PDF tools for finished materials |

Each skill describes its actual inputs, outputs and limits. These are workflows and selected helpers, not a complete production application or an installation guarantee. No paid accounts or model services are included.

## Evidence and public release scope

This edition excludes client information, real product models, unpublished inventions, formulas, internal control protocols, production parameters, server configurations, accounts and secrets. Equipment and patent workflows include general methods and blank templates; they establish no product safety validation, filing or grant. Check licenses for external materials separately.

Validation covers structure, links, private-data patterns, bilingual content, selected synthetic helper tests and scenario reviews. Real video production, product rendering, production deployment, hardware integration and formal applications still require project-specific verification. See [release and validation scope](CHANGELOG.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

## Frequently asked questions

### What are Longevity Skills?

Longevity Skills is a collection of eleven open-source AI agent skills maintained by LONGEVIS. Each installable folder uses a `longevity-*` name and contains English and Chinese workflow instructions, references and selected helpers. The [skill catalog](catalog.json) lists the names, entrypoints and dependencies.

### Who is behind this repository?

[LONGEVIS 朗静岛](https://www.longevis.net/), a biohacking and longevity hardware solutions company, maintains this collection through the [lijian19893333-boop GitHub account](https://github.com/lijian19893333-boop). The workflows come from our own product design, content creation, digital interfaces and delivery work. Contact: [248234067@qq.com](mailto:248234067@qq.com).

### Do I need to work in longevity or biohacking to use these skills?

You can adapt the general workflows to other products and industries. For example, use reference-based Blender modeling for a physical product, science-video planning for an educational topic, or website release checks for an authorized web project. Supply your own references, confirmed facts and tool access.

### Can I use them for commercial projects?

Original repository documentation, helpers and examples use the [MIT License](LICENSE), which permits commercial reuse subject to its terms. Keep the license and required notices. Third-party code and external assets retain their own terms; check [third-party notices](THIRD_PARTY_NOTICES.md).

### Where can I get help or contribute?

Use the [bilingual issue forms](https://github.com/lijian19893333-boop/longevis-creative-production-skills/issues/new/choose), read the [contribution guide](CONTRIBUTING.md), and follow the [public community roadmap](https://github.com/users/lijian19893333-boop/projects/1). The [Wiki](https://github.com/lijian19893333-boop/longevis-creative-production-skills/wiki) brings together company background, installation examples and skill links.

## License and contributions

Original repository documentation, helper scripts and examples use the [MIT License](LICENSE). Third-party viewer code retains its own copyrights and licenses. This repository grants no rights to external brand identities or project assets. Issues with reproducible inputs and PRs explaining purpose, checks and dependencies are welcome.
