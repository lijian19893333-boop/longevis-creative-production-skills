# Multi-view Comparison and Acceptance

## Inspection order

Check outlines and clear space, then component relationships, then visual details.

| View/state | What to inspect |
|---|---|
| Front | Overall height/width, display position, door width, relative logo/grip/grille size |
| Left/right | Depth, sloped planes/breakpoints, protrusion, equipment position, display tilt |
| Rear | Cabinet door partitions, open areas, columns, ventilation |
| Top | Inner/outer contours, wall thickness, cavity, closed doors, display footprint |
| Bottom | Closed floor, casters/supports, platform position |
| Open door/interior | Hinge, attached parts following the door, seal, platform, lining, outlets |
| Other configurations | Layout, color, glass printing, light color; changing filenames is insufficient |

A direction without evidence cannot be counted as matched, but still inspect the geometry for intersections and missing faces.

## Fair registration

Retain the reference, model render, and overlay side by side. Use uniform scale and explicit anchors for each common view. Translation aligns the floor/center; independently moving individual components in the comparison image hides errors. Do not use nonuniform stretching, liquification, optical-flow warping, or individual component scaling. Change the model or the evidence-calibrated camera.

Determine scale from dimensions and camera parameters. For example, a 2 m orthographic image height rendered at 1000 px gives 500 px/m; a 1.8 m reference occupying 900 px has the same scale. These are mathematical examples, not product dimensions. Do not renormalize against the incorrect model's current bounding box each round and erase the dimensional error being measured.

Separate silhouette masks from feature lines. Matching outlines can hide incorrect doors, UI, or interiors. Highlights, textures, and shadows can create color edges that are not physical boundaries. If the source is uncertain by 1–2 px, record that uncertainty instead of changing dimensions to chase noise.

## Included silhouette tool

Inputs must be grayscale PNG masks with a black background and white product region. Generate these reliably from suitable views; do not mistake a bright product for background. Install Pillow, then run from this skill directory:

```sh
python3 scripts/compare_masks.py --reference ref_mask.png --model model_mask.png --scale 1 --reference-anchor 300 900 --model-anchor 300 900 --basis "Same projection, 500 px/m; floor-center anchors" --output qa/front
```

The scale maps model pixels to reference pixels. Anchors are explicit `(x, y)` pixels in their respective images. Outputs are `overlay.png` (red: reference only; blue: model only; purple: overlap), `model-aligned.png`, and `report.json`. IoU measures overlap in this projection only. It does not establish interior structure, all views, manufacturing dimensions, or overall model quality.

## Iteration and stopping

For each iteration record the largest discrepancy, changed component, and rechecked views. Use a reproducible script or explicit component edits and preserve a rollback version. A door-width change affects front/top/open-door checks; wall thickness affects clearance and closure; material changes require front and oblique views.

If the discrepancy stops improving, check reference correspondence, scale, camera, normals, and occlusion before adding detail. When no new evidence emerges and remaining differences are within reference precision, record the limits and deliver verified results instead of retrying indefinitely.

If there is a deadline, freeze a reviewable version beforehand and distinguish completed work from unfinished/unverified items. Time pressure does not make a review model an exact engineering deliverable.

## Final checks

Measure units and overall dimensions. Check finite coordinates, unintended duplicate faces, intersections, normals, UVs, and components that should be closed solids. Do not flag reasonable thin glass surfaces with an indiscriminate “everything must be solid” rule.

Check changed material indices, exported textures, and animations. Inspect every final render and enlarge critical regions; inspect the same version in a real browser. Record model, texture, render, and viewer versions/hashes in the delivery manifest and confirm refresh loads the current files. Report geometry checks, interaction checks, and remaining visual differences separately; none substitutes for the others.
