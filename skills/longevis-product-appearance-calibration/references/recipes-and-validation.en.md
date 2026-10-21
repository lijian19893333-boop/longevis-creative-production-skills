# Recipes and Validation

[中文版](recipes-and-validation.md)

## Scope and command

`apply_glb_recipe.py` applies explicit appearance changes without changing geometry. It requires Python 3 and no third-party packages. Input is GLB 2.0 with at most one embedded buffer; external buffer URIs and extra unknown chunks are unsupported. Ensure the input is valid and any external image dependencies resolve first. This tool is not a complete glTF validator and does not decode images.

It does not decide visual quality, generate UVs, decimate meshes, interpret compression or advanced-extension semantics, or replace visual acceptance. Apply recipes only to understood material/texture/light fields supported by the target viewer. A material change does not ensure every alternate material in a material-variant extension changes too.

Generate a separate output from an immutable backup:

```bash
python3 scripts/apply_glb_recipe.py original.glb recipe.json calibrated.glb --report report.json
```

Existing outputs are refused. Use `--overwrite` only after confirming that output may be replaced; do not use the source file as output. Keep the report path separate from the model, source, and recipe to avoid overwriting another file. Read recipes, image files, and sources only from trusted local files; the helper does not download resources or execute recipe code.

## Example recipe

All names and values below demonstrate the format; they are not measurements for any product. The operator must supply a real usable PNG at `textures/wood-normal.png`; no texture is bundled.

```json
{
  "id": "example-calibration-r1",
  "note": "Identify the approved reference and reason for calibration",
  "textures": {
    "wood_normal": {"file": "textures/wood-normal.png", "mimeType": "image/png"}
  },
  "materials": {
    "Exact material name": {
      "remove": ["alphaMode"],
      "set": {
        "pbrMetallicRoughness": {"metallicFactor": 0, "roughnessFactor": 0.42},
        "normalTexture": {"index": "wood_normal", "scale": 0.3}
      }
    }
  },
  "lights": [{
    "name": "Example lamp", "type": "point",
    "color": [1, 0.1, 0.05], "intensity": 0.65,
    "range": 2.3, "translation": [-0.4, 1.7, 0],
    "group": "interior", "controlMaterial": "Exact emitter material name"
  }]
}
```

- `id` is the required recipe version. Reapplying the same id to an already marked model copies it unchanged, without duplicating lights/textures or rerunning modifications. Change the id when changing recipe content, or generate again from the original backup. Matching ids alone do not prove matching content.
- `source_sha256` is optional and must contain the full original-file SHA-256. An idempotent rerun checks the recorded original-source hash.
- `materials` selects exact material names. Unknown names are refused; duplicate names are refused unless top-level `match_all_material_names: true` explicitly opts into all matches. The report lists actual indices.
- `set` recursively merges dictionaries and replaces other values; `remove` deletes dot-separated field paths. To replace an entire nested object, remove it before setting the replacement so old fields do not remain.
- Texture paths are relative to the recipe. MIME defaults to `image/png`; set `image/jpeg` explicitly for JPEG. The operator verifies actual image format, decodability, and UVs. Color maps use sRGB; normal/ORM maps use non-color data. ORM channels are R=occlusion, G=roughness, B=metallic. The glTF field is `pbrMetallicRoughness.metallicRoughnessTexture`, not `roughnessTexture`.
- String texture indices can name textures added by this recipe; use valid integer indices for existing textures. Unresolved names and out-of-range indices are refused. Supply a texture's optional `sampler` object when needed.
- `lights` adds `KHR_lights_punctual` lights and scene nodes. `translation` and optional `rotation` belong to the node. Choose intensity, range, and position for the asset's actual units and renderer. `group` and `controlMaterial` produce node extras only; no switch integration is automatic. Other light fields follow glTF light format; the helper does not perform full semantic validation.

## Validation and rollback

Before writing, the helper checks unchanged meshes/accessors/animations/skins declarations, existing nodes, and the original BIN prefix. New images are appended. This does not establish correct UVs, light placement, visible door motion, or final viewer behavior. Run structural tests first, then inspect the actual browser and native rendering paths.

```bash
python3 scripts/test_apply_glb_recipe.py
```

Bundled tests use an authored triangle, synthetic door animation, and tiny PNG. They check binary and geometry/animation preservation, texture/light addition, idempotency, hash mismatch, unknown/duplicate materials, unresolved textures, external buffers, existing outputs, and refusal to overwrite the source with a report. No real product assets are included, and complete production visual validation is not claimed.

For each configuration, record model, configuration, actual URL, old/new SHA, recipe, before/after images, verified operations, missing items, and runtime-copy status. Preserve original model, viewer, and configuration backups. Roll back model, viewer, cache fingerprints, and index together. Record status separately for both display chains, every authorized configuration, and each function; a few screenshots do not replace full acceptance.
