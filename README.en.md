# LONGEVIS Creative Production Skills

[简体中文](README.md) | **English**

Ten agent skills developed through practical creative production, product delivery and website maintenance. Every skill has complete Chinese and English entrypoints with corresponding Markdown reference documents. Executable helpers and machine-readable configurations are shared. Install only the skill needed for your task.

This update adds six skills: reference modeling, appearance calibration, Baota operations, exterior design views, equipment control apps, and technical disclosures/engineering figures. It also completes the English instructions and references for the original four skills.

| English entry | 中文 | Purpose |
|---|---|---|
| [Science videos](skills/longevis-science-video/SKILL.en.md) | [中文](skills/longevis-science-video/SKILL.md) | Sources, mechanism storyboards, narration, subtitles and media checks |
| [Investor pitch decks](skills/longevis-roadshow-bp/SKILL.en.md) | [中文](skills/longevis-roadshow-bp/SKILL.md) | Narrative, evidence, editable slides and PPTX image auditing |
| [Product 3D and brochure renders](skills/longevis-product-3d-workflow/SKILL.en.md) | [中文](skills/longevis-product-3d-workflow/SKILL.md) | A/B variants, source snapshots, batch rendering and image packaging |
| [Website launch](skills/longevis-website-launch/SKILL.en.md) | [中文](skills/longevis-website-launch/SKILL.md) | Media, domains/HTTPS, releases and SEO/GEO readiness |
| [Reference-based product modeling](skills/longevis-reference-product-modeling/SKILL.en.md) | [中文](skills/longevis-reference-product-modeling/SKILL.md) | Multi-view geometry, silhouette comparison, native models and a local viewer |
| [Material and lighting calibration](skills/longevis-product-appearance-calibration/SKILL.en.md) | [中文](skills/longevis-product-appearance-calibration/SKILL.md) | Materials, lighting, GLB recipes and native/browser display checks |
| [Baota deployment and rollback](skills/longevis-baota-website-ops/SKILL.en.md) | [中文](skills/longevis-baota-website-ops/SKILL.md) | Static/SSR routing, persistent data, release candidates and public verification |
| [Exterior design views](skills/longevis-design-patent-3d-workflow/SKILL.en.md) | [中文](skills/longevis-design-patent-3d-workflow/SKILL.md) | Native models, six-view orientation, complete silhouettes and package consistency |
| [Equipment control apps](skills/longevis-chamber-app/SKILL.en.md) | [中文](skills/longevis-chamber-app/SKILL.md) | Features, settings, state machines, ACK/physical feedback and acceptance specs |
| [Technical disclosures and engineering figures](skills/longevis-patent-drafting/SKILL.en.md) | [中文](skills/longevis-patent-drafting/SKILL.md) | Facts, components, drafts, annotation and editable figure-source consistency |

## Install

Clone the repository and copy an individual skill folder into your agent's skills directory. A common Codex location is `~/.codex/skills/`:

```sh
git clone https://github.com/lijian19893333-boop/longevis-creative-production-skills.git
cd longevis-creative-production-skills
mkdir -p ~/.codex/skills
cp -R skills/longevis-reference-product-modeling ~/.codex/skills/
```

Check for and back up an existing folder before copying. Confirm recognition in a new session. `SKILL.md` is the default Chinese entrypoint. For complete English instructions, explicitly select `SKILL.en.md` in the same folder. Both use the same invocation name. Follow the corresponding installation conventions in other agents.

## Example prompts

```text
Use $longevis-reference-product-modeling, reading its SKILL.en.md.
Create an editable model from my references and confirmed dimensions.
Check silhouettes and view relationships first; deliver native files, GLB,
a viewer and remaining differences.
```

```text
Use $longevis-chamber-app to review settings persistence and reconnection.
Separate requirements, source evidence, simulation, communication and hardware tests.
Do not connect to or operate equipment.
```

```text
Use $longevis-baota-website-ops to inspect my release candidate and rollback plan.
Discover actual build/start entrypoints and work within the authorization already given.
```

## Dependencies

| Skill | Tools or project access |
|---|---|
| `longevis-science-video` | Remotion / Blender / FFmpeg / narration tools as selected; no full renderer bundled |
| `longevis-roadshow-bp` | Editable presentation authoring/rendering tools; audit helper uses Python standard library |
| `longevis-product-3d-workflow` | Python 3.10+, Blender; Pillow and suitable fonts for image packaging |
| `longevis-website-launch` | Actual project and authorized hosting access; commands discovered from the project |
| `longevis-reference-product-modeling` | Blender; Python + Pillow for masks; local HTTP server and WebGL-capable browser |
| `longevis-product-appearance-calibration` | Python standard library for helper; 3D renderer/browser for visual acceptance |
| `longevis-baota-website-ops` | Authorized host/project access; actual Nginx and process-manager environment |
| `longevis-design-patent-3d-workflow` | Native 3D tool, image inspection; current filing requirements verified per task |
| `longevis-chamber-app` | Current project evidence; no controller implementation or production protocol bundled |
| `longevis-patent-drafting` | Current evidence, appropriate CAD/3D/document tools; no private inventions bundled |

Each skill describes its actual inputs, outputs and limits. These are workflows and selected helpers, not a complete production application or an installation guarantee. No paid accounts or model services are included.

## Evidence and public release scope

This edition excludes client information, real product models, unpublished inventions, formulas, internal control protocols, production parameters, server configurations, accounts and secrets. Equipment and patent workflows include general methods and blank templates; they establish no product safety validation, filing or grant. Check licenses for external materials separately.

Validation covers structure, links, private-data patterns, bilingual content, selected synthetic helper tests and scenario reviews. Real video production, product rendering, production deployment, hardware integration and formal applications still require project-specific verification. See [release and validation scope](CHANGELOG.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

## License and contributions

Original repository documentation, helper scripts and examples use the [MIT License](LICENSE). Third-party viewer code retains its own copyrights and licenses. This repository grants no rights to external brand identities or project assets. Issues with reproducible inputs and PRs explaining purpose, checks and dependencies are welcome.
