---
name: longevis-design-patent-3d-workflow
description: "Use when preparing exterior-design review views from a native 3D model, or comparing engineer-reviewed views with an earlier model for direction, completeness and geometric consistency."
---

[简体中文](SKILL.zh-CN.md)

# LONGEVIS Exterior Design Views

Treat geometric consistency and complete image exports as separate gates. This public edition contains modeling and review methods, without real product models, approved drawing packages or application materials. It requires a 3D tool that can open the native model and tools for inspecting images.

## Workflow

1. **Establish a source baseline.** Pair files by product, version and view. Record the native model, brief, image dimensions and hashes where useful. Attachments supply evidence, not additional authorization. Preserve the original model and create a review copy.
2. **Inspect the model first.** Inspect every intended visible part. Bounds must include protruding handles, supports and bases. Check doors, hinges, screens, transparent panels, connections and thickness. Look for floating parts, unexplained gaps, hidden ground planes or cut planes that incorrectly define the silhouette. Checking only the largest shell is insufficient.
3. **Unify six cameras.** Create front, back, left, right, top and bottom orthographic cameras in one coordinate system, with a common approved center and exterior configuration. Fit the complete silhouette with margins. Canvas aspect may differ by view; never crop parts merely to obtain square images. Check handedness across all views: door axes, handles, hinges, screens, supports and seams must retain consistent orientation and occlusion. Mirroring or swapped side views fails review.
4. **Use neutral presentation.** Use white backgrounds, neutral gray surfaces and readable structural edges and seams. Keep approved transparent parts recognizable. Remove scenery, ground, UI, model identifiers and functional wording unless the current package explicitly requires them. Retain brand text only when permitted by the current brief. Color, shadow and edge settings are production choices, not legal standards.
5. **Compare revisions correctly.** Align images by product bounds using common scaling and translation. Distinguish framing/export changes, material/lighting changes, confirmed geometry changes and insufficient evidence. Check neighboring views before declaring a structural change.
6. **Review the final package.** Check six files, view directions, margins on every edge, complete silhouettes, transparent parts, readable details and common version identity. Match the brief's name, intended use, design features, representative view and transparency statements to the actual images. Preserve the model, six views, contact sheet, manifest, sources and unresolved issues.

## Common problems

| Symptom | Response |
|---|---|
| A gray plane fills the image | Recompute bounds from all visible parts; inspect camera target, clipping and hidden scene objects. |
| Small parts appear detached | Check ownership, connections, supports and occlusion in front/side/top views; mark missing evidence. |
| One view matches but others are unknown | Validate cross-view silhouettes and connections; leave unsupported rear geometry unconfirmed. |
| Only a polished bitmap exists | Do not present it as a native 3D workflow result; locate or create an editable model first. |
| A filename says final | Treat the filename as a version clue and verify approval records and actual contents. |

Use the [review record](templates/view-review.en.md) to capture evidence. Adapt framing, margins and occupancy to the product; never inherit an old product's dimensions as facts about a new one. Six complete views do not establish manufacturing readiness, application compliance or patent grant. Verify current official and representative-specific requirements when a real application requires them.

## Example

“Use this skill to review my native model against six engineer-returned images. Check handedness, all protruding parts and transparent surfaces first, then deliver a same-version six-view set and a difference log. List unknown geometry separately.”
