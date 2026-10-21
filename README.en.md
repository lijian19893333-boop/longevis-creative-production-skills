# LONGEVIS Creative Production Skills

[简体中文](README.md) | **English**

Four agent skills for science videos, investor pitch decks, product 3D workflows, and website launches.

This collection connects evidence checks, editable production, and delivery verification. It provides workflow instructions, selected helper scripts, and configuration examples. Producing a finished video, deck, model, or website also requires the relevant tools and project materials.

## Skills

| Skill | When to use it | Included resources |
| --- | --- | --- |
| [longevis-science-video](skills/longevis-science-video/SKILL.md) | Plan science explainers, build mechanism animations, prepare narration and subtitles, and verify video exports | Workflow and brief example; no complete rendering application |
| [longevis-roadshow-bp](skills/longevis-roadshow-bp/SKILL.md) | Create or redesign investor pitch decks while retaining substantive information | Investor narrative, visual production guidance, and a PPTX image audit script |
| [longevis-product-3d-workflow](skills/longevis-product-3d-workflow/SKILL.md) | Iterate on product models and variants, render multiple views, and package brochure images | Blender batch rendering, source snapshots, image packaging, and example configurations |
| [longevis-website-launch](skills/longevis-website-launch/SKILL.md) | Prepare website releases, optimize media delivery, deploy to Baota/ECS, switch domains or HTTPS, and verify SEO/GEO readiness | Deployment runbook and release record template; no production configuration |

## Install in Codex

Clone this repository, then copy the individual skill folders you need into your Codex skills directory. A common location is `~/.codex/skills/`.

```sh
git clone https://github.com/lijian19893333-boop/longevis-creative-production-skills.git
cd longevis-creative-production-skills
mkdir -p ~/.codex/skills
cp -R skills/longevis-roadshow-bp ~/.codex/skills/
```

Check for an existing folder with the same name and back it up before copying. Open a new session and confirm that the skill is recognized. For other agents, follow that environment's skill installation instructions.

Each skill is independent. You can install one without installing the rest of this collection. External production tools remain separate requirements.

## Example prompts

```text
Use $longevis-science-video to create a 60-second explainer about how sound travels.
Verify the sources, produce a reviewable draft, and deliver subtitles and an editable storyboard.
Write the narration in English.
```

```text
Use $longevis-roadshow-bp to turn the project materials into a 12-slide investor pitch deck.
Keep important facts, leave editable placeholders for unknown numbers, and put the funding ask last.
Write the deck in English.
```

```text
Use $longevis-product-3d-workflow to create A/B product variants from my references and dimensions.
Preserve the source models, render representative proofs first, then export PNG/JPG images and contact sheets.
```

```text
Use $longevis-website-launch to inspect my website release candidate.
Verify the build, backups and rollback plan, deploy within the authorization provided,
and deliver a record of checks against the public website.
```

## Language support

This README provides an English overview, installation instructions, examples, and dependency information. The detailed skill instructions and most reference documents are currently written in Chinese. You can request English or another output language in your prompt; this repository does not claim to provide complete English translations of every skill document.

## Requirements and limits

- **Science video:** Depending on the project, prepare Remotion / Three.js, Blender, FFmpeg, and narration tools. This repository does not include a complete video renderer or paid service accounts.
- **Investor pitch deck:** Requires editable presentation authoring and rendering tools. `audit_pptx.py` uses the Python standard library and detects byte-identical image reuse and missing references. It does not assess visual similarity or design quality.
- **Product 3D:** General scripts require Python 3.10+. Render scripts run inside Blender Python. Image packaging requires Pillow and a font covering the labels. Adapt example dimensions, object names, camera positions, and paths to your models.
- **Website launch:** Requires access to the actual project and hosting environment. Discover build and deployment commands from that project. No credentials, production configuration, or website application source is included.
- Examples are workflow demonstrations, not verified business figures, manufacturing conclusions, medical claims, or funding commitments. Successful file generation and user acceptance are separate milestones.

The current release has had syntax, internal link, and selected helper-script checks. Full video production, Blender rendering, and installation on other devices have not been verified for this public package.

## Public release scope

Local project paths, private narration history, real commercial case images, production deployment records, and project-specific parameter notes have been removed. Source models, film projects, customer records, and commercial presentation files are not included.

## License

All skill documentation, scripts, and examples in this repository are released under the [MIT License](LICENSE). Use, modification, redistribution, and commercial use are permitted subject to retaining the copyright and license notice. External tools, models, assets, and services keep their own licenses.
