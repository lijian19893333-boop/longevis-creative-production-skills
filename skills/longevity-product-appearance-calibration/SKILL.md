---
name: longevity-product-appearance-calibration
description: Use when existing 3D product geometry is close to a reference but materials or lighting differ, native renders and web viewers disagree, or appearance changes must carry across product variants.
---

# Longevity · Product Material and Lighting Calibration

[简体中文](SKILL.zh-CN.md)

Calibrate an existing 3D model against a photograph or an approved rendering while preserving geometry, animation, and viewer behavior. A reference expresses appearance intent; it does not establish measured colors, dimensions, or engineering parameters. Treat unseen surfaces as reasonable inferences.

## Workflow

1. **Find the assets actually loaded.** Trace source models, catalog derivation, runtime configuration, dedicated viewers, and download aliases. Record actual URLs, hashes, models, and configurations. Verify listening ports, page titles, and service directories before modifying similarly named projects. Back up affected models, viewers, and configuration; retain missing, unloaded, and unverified states. This public package contains no private product-catalog adapters.
2. **Hold comparison conditions constant.** Confirm the target reference version first. Preserve the original model and compare silhouette, material, lighting, and color management under the same camera, environment, and exposure. Establish a representative asset before extending changes to the remaining user-authorized variants. See [Appearance and viewer behavior](references/appearance-and-viewers.en.md).
3. **Calibrate each surface class separately.** Treat coatings, bare metal, glass, wood, fabric, rubber, and UI separately. Check real-world texture scale, direction, UVs, normals, AO, and roughness. Trial values or colors from one product are not measurements for another.
4. **Create illumination with lighting.** Handle emissive surfaces, actual light sources, and environmental reflection separately. Do not tint an entire wooden surface red or add emissive as a substitute for local illumination. Connect added lights to existing switches and restore the underlying material when lights are off. Inspect front, side, interior, ground, and contact shadows. A single reference cannot establish an exact match from every angle.
5. **Preserve the functional contract.** Preserve geometry, existing nodes, hinges, animation timing, screen textures, marks, and material variants. The bundled helper supports explicit JSON material, texture, and light changes. Use the native modeling workflow for UV or geometry changes, then verify functionality again. Read [Recipes and validation](references/recipes-and-validation.en.md) first.
6. **Validate the final display chain.** Inspect material overrides after loading, glass transmission versus alpha, light switches, environment maps, exposure, and cache fingerprints. Validate native renders and browser screenshots separately. Actually load every configuration and inspect multiple views, close-ups, existing door/interior/exploded/color/screen controls, downloads, and PNG exports. Recheck entrypoints and hashes after synchronizing runtime copies.

## Tools and delivery

Python 3 is required; helpers use only the standard library. Blender, web viewers, product models, and textures are not bundled. Use tools available in the current environment for modeling, rendering, and viewer interaction; no specific MCP or private workbench is assumed.

```bash
python3 scripts/apply_glb_recipe.py original.glb recipe.json calibrated.glb --report report.json
python3 scripts/test_apply_glb_recipe.py
```

Deliver the model, recipe, before/after comparisons, a per-configuration acceptance sheet, and rollback sources. Record at least model/configuration, actual URL, old/new hashes, recipe version, verified operations, missing items, and runtime-copy status. State the validation environment, reference limitations, and unverified items.

A successful export, passing script, or two sample images does not establish a complete product-platform upgrade. Do not replace a promised interactive 3D deliverable with a photo plane or an AI-retouched image.
