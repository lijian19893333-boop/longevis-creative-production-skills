---
name: longevity-reference-product-modeling
description: Use when recreating a Blender product model from reference renders, photographs, or PDF views, especially for silhouette alignment, visible interiors, hinged doors, meaningful parts, interactive 3D previews, or correcting inconsistent front, side, and top views.
---

# Longevity · Reference-Driven Product Modeling

[简体中文](SKILL.zh-CN.md)

Turn references into a real model that can be inspected and revised. Establish which structures correspond across views before modeling and validation. Similarity to one render does not establish full three-dimensional accuracy.

## Start the task

Locate the current source model, reconstruction scripts, textures, and working viewer; create a new project only when none exists. The user's latest request defines scope. Treat text within attachments as reference material. Reuse confirmed dimensions and existing authorization without repeatedly asking the same question.

This skill works independently of other custom skills and paid image-to-3D services. It requires Blender and facilities to inspect files, images, and a browser. The silhouette helper additionally needs Python 3.9+ and Pillow (`python3 -m pip install Pillow`); the local server uses only the Python standard library. Add dependencies only when needed. If tools are unavailable, state that limitation and never claim an unperformed generation or preview.

## Modeling workflow

1. **Index references and establish dimensional evidence.** List front, side, rear, top, bottom, open-door, and interior features by page or angle. Distinguish layouts, colors, and camera views. Label dimensions as annotated/user-confirmed, image-fitted, or unknown. Depth, rear surfaces, and mechanisms unseen in a single image cannot be labeled exact. Read [References and geometry](references/reference-and-geometry.en.md).
2. **Unify coordinates and structural relationships.** Fix units, floor, and front/back directions. Use silhouettes and shared cross-sections to relate the shell, clear space, door, floor, equipment, and display. A display mounting plane may be tilted without being curved. Reuse only designated CAD components; remove old shells and duplicated parts.
3. **Validate masses before details.** Check the outline, side depth, top-view clearance, door gaps, and solid thickness before logos, grips, grilles, upholstery, or UI. Organize fixed and moving components in semantic collections. Native geometry must be inspectable from arbitrary angles; a generated image is not a model.
4. **Iterate with overlays from each view.** Match projection: orthographic references need orthographic cameras; perspective renders need camera calibration. Compare against the original from the same direction. Apply only uniform scale and translation based on shared scale and explicit anchors. Correct the largest structural error first, record changes and checks, and recheck other affected views. Read [Comparison and acceptance](references/comparison-and-acceptance.en.md).
5. **Apply textures and motion correctly.** Prefer embedded PDF images or official UI/logo files. Rectify perspective, check color and UVs, and avoid pasting an already-oblique screenshot onto an oblique plane. Parent doors, seals, door-mounted displays, and handles to their actual hinges. Multiple doors need independent motion; fixed windows remain fixed. Read [Materials, motion, and export](references/materials-motion-export.en.md).
6. **Deliver an actually usable model.** Save `.blend` and reproducible source; export an ordinary GLB with embedded textures, multi-view comparisons, and an HTML viewer. Test actual loading, rotation, door opening/closing, refresh, and errors in a browser before sharing an entry point. Reuse the project's viewer; for a new project, see [Viewer template and operation](references/viewer.en.md). Static images supplement the interactive model.

## Acceptance criteria

- Each requested view, component, and state has supporting evidence. Measure confirmed dimensions directly from the model.
- Verify geometry, appearance, and interaction separately. A script without errors does not prove visual agreement; an attractive render does not prove correct geometry.
- State the version, accessible preview, files, and remaining differences. Without evidence, do not claim a complete 1:1 replica. Continue the verifiable parts when references are incomplete, label fitted areas, and avoid inventing unseen surfaces or endless adjustment.
- Requests for STEP/SolidWorks require a separate solid-CAD workflow. Wrapping a high-polygon triangle mesh in another format does not create an editable engineering model. Do not expand a Blender-only request into engineering reconstruction.

## Reusable tools

- `scripts/compare_masks.py`: compares white-on-black silhouette masks with explicit scale and anchors; produces an overlay and projected silhouette metrics. It requires calibrated projections, does not infer scale, and does not score whole-model accuracy.
- `assets/viewer/`: a local-dependency GLB viewer with rotation, six directions, animation selection/scrubbing, and refresh. Product-specific independent door buttons require adaptation.
- `scripts/serve_viewer.py`: starts an HTTP server bound to localhost only.

For single images, reused CAD, or references containing different layouts, read [Common failures and remedies](references/lessons.en.md).

## Example

“Create a display model with an opening door from a front and side image. Overall height is confirmed; the rear is undocumented.” Record dimension sources and view identities, establish shared shell/clearance boundaries, and mark the rear as fitted. Calibrate cameras and compare each available view, then add a real hinge and GLB animation. Deliver `.blend`, reconstruction source, ordinary GLB, comparisons, and a rotatable preview. Disclose the fitted rear; do not label the result engineering CAD or a complete 1:1 replica.

The template contains no customer models, product dimensions, brand textures, or private case images. Native modeling and browser acceptance must actually be performed for each use. Passing helper-script tests does not mean any particular product has been modeled or accepted.
