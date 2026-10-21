# Script Interfaces

[中文版](script-interfaces.md)

Requires Python 3.10+. Blender scripts target Blender 4.2+/5.x; verify the exact version and GPU backend in the user's environment. Image packaging also requires Pillow. Rendering runs in Blender Python; other scripts run in ordinary Python. Discover existing dependencies before downloading software or changing global settings.

## Prepare the job

Copy `assets/render-job.example.json` and `assets/studio_recipe.py` into the project working directory. Rename the example JSON to `render-job.json` and adjust source paths, versions, component selectors, and shots. Example cameras suit a 2200×1800×2000 mm chamber; recompose for other products.

All relative paths resolve from the JSON directory, not the shell working directory. Do not generate project files inside the installed skill's assets directory.

Main fields:

| Field | Purpose |
| --- | --- |
| `variants[].id` / `label` | ASCII file identifier / display name, which may include Chinese |
| `source` / `version` | Native `.blend` path / version label |
| `dependencies` | Files affecting rendering, such as unpacked textures; may be global or per variant |
| `recipe` | Optional local Python recipe exposing `configure(scene, job, variant, shot)` |
| `shots[].size` | Output pixels; set landscape and portrait separately |
| `camera` | `location`, `target`; `lens` or `ortho_scale` |
| `shots[].variants` | Optional list of variant IDs using the shot |
| `shots[].samples` | Optional per-shot final sample ceiling |
| `shots[].frame` | Animation frame; defaults to frame 1 |
| `render` | Samples, bounces, adaptive threshold, threads, exposure, view transform |

Recipe fields: `hide.names/prefixes/contains/collections` control render visibility. Missing exact object/collection names cause errors; inspect matches for prefixes and substring selectors yourself. `object_rotations_degrees` supplies absolute XYZ Euler angles for named objects. `material_overrides` uses exact material names and Principled BSDF input names. `studio.scale` scales studio lighting placement/energy, not the product or cameras.

Fill a transmission override only after identifying the material:

```json
{"material_overrides":{"Clear PC":{"Alpha":1,"Transmission Weight":1,"Roughness":0.022}}}
```

Recipes are executable local Python. Rendering fingerprints include the recipe file; add its other dependencies to `dependencies`. The script does not modify source `.blend` files; custom recipes must not save over them.

## Render

Below, `product_skill_dir` denotes the installed skill directory and `blender` the discovered Blender executable. A common macOS path is `/Applications/Blender.app/Contents/MacOS/Blender`.

```bash
blender --background --factory-startup --python-exit-code 1 --python "$product_skill_dir/scripts/render_batch.py" -- /project/render-job.json --proof --variants A --shots 01_hero,05_interior
blender --background --factory-startup --python-exit-code 1 --python "$product_skill_dir/scripts/render_batch.py" -- /project/render-job.json --variants A --shots 01_hero
blender --background --factory-startup --python-exit-code 1 --python "$product_skill_dir/scripts/render_batch.py" -- /project/render-job.json --resume
```

`--device AUTO` discovers an available GPU and otherwise uses CPU. Explicit choices are `CPU`, `METAL`, `OPTIX`, `CUDA`, `HIP`, and `ONEAPI`. An unavailable explicit backend stops execution instead of silently switching.

`--python-exit-code 1` makes script exceptions return failure, avoiding misreading Blender's default process exit status as success.

Images go to `raw/<variant>/<shot>.png`, proofs to `proofs/`. `.records/` stores completion, cameras, elapsed time, input fingerprints, and PNG hashes. New images use separate temporary files and replace targets only after validation, avoiding accidental reuse of old files after interruption.

`manifest-final.json` or `manifest-proof.json` summarizes completed records matching the current configuration. Partial shot runs have `complete: false`. Missing, damaged, or changed-configuration images rerender under `--resume`. Changing one camera invalidates only that shot; changing the global studio recipe invalidates all shots.

Run only one batch process per output directory to prevent concurrent manifest writes. When stopping, manage only render processes launched for this task; preserve records and resume later. Do not edit records to mark interrupted images complete.

The scripts do not automatically establish local-geometry equivalence between models. Verify shared-interior reuse separately and record its source; otherwise render independently.

## Package images

```bash
python3 "$product_skill_dir/scripts/package_images.py" /project/renders/brochure/manifest-final.json --out /project/delivery/brochure
```

The packager refuses incomplete manifests, proof manifests, duplicate shots, and image hash mismatches. It creates `PNG/`, `JPG/`, `overview/`, `image-manifest.json`, `usage.txt`, and `brochure-images.zip` from read-only originals without changing raw images. The ZIP replaces its target only after CRC validation.

Defaults add sRGB ICC and 300 dpi metadata without upscaling. `--dpi` sets layout density; `--font` supplies a font supporting labels. Missing suitable Chinese fonts produce an explicit error rather than square placeholder glyphs.

## Source snapshots

```bash
python3 "$product_skill_dir/scripts/model_snapshot.py" create /project/baseline.json --root /project/variants/A/v2
python3 "$product_skill_dir/scripts/model_snapshot.py" verify /project/baseline.json
```

Creation selects common model/source/texture suffixes; adjust them with `--suffixes`. Verification requires original files to be unchanged/present and reports additions; `--strict` treats additions as differences too. `--root` supports checking a copied/moved directory. If the snapshot already exists, choose another name to preserve the baseline.
