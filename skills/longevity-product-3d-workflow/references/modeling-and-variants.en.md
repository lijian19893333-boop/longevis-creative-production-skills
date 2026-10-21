# Modeling and Variant Iteration

[中文版](modeling-and-variants.md)

Define dimensions and component configuration centrally in the source entrypoint. UI labels, export descriptions, and checks should read the same parameter source.

One possible coordinate convention is X left/right, Y front/back, Z up, with front at −Y and right wall at +X. This is a project convention, not the only valid one. glTF export commonly converts to Y-up; verify viewer pivots and cameras after conversion.

| Request | Implementation |
| --- | --- |
| Front width | State which face is measured instead of relying on an assumed length/width order |
| Widen the door frame | Compute frame envelope, panel, and clear opening separately; one value must not overwrite all three |
| Handle on the door's right, away from the frame | Record center position, edge clearance, and grip space; inspect both sides |
| Hinges inside, door opens inward | Separate fixed/moving parts; rotate around the real axis and check swept space |
| Sofa back against the right interior wall | Transform the back direction and furniture bounds into world coordinates; check door movement and circulation |
| Screen size in inches, 16:9 | Inches describe the diagonal; record active display area and device bezel separately |
| Three lining sections with upper/middle/lower colors | Use three continuous panels and two fine surface seams, not many small blocks or actual open gaps |

For a 16:9 active display: `d_m = diagonal_inch × 0.0254`, `w = d_m × 16/√337`, `h = d_m × 9/√337`. State the rotation for portrait placement rather than confusing 9:16 with landscape.

## Objects, materials, and movement

Suggested collections: `Body`, `Frame`, `Door`, `Window`, `Lining`, `Furniture`, `Devices`, `Ceiling`, `Studio`. Names may differ but must support stable selection instead of depending on object indices.

Parent the door panel, both handles, and moving hinges to a common pivot; fixed hinges belong to the chamber. Inspect closed, half-open, and fully open states and collisions with furniture, floor, or frame throughout motion.

Express thickness in geometry; coatings, leather, wood, metal, and transmission in materials. Pack textures or list external dependencies. Web transparency can differ from offline ray tracing; record render-specific transmission adjustments and preserve the source file.

For pressure shells, structural profiles, or locks, record user-specified values and illustrative assumptions. Appearance models do not replace strength calculations, connection design, manufacturing drawings, or test conclusions. Define a separate engineering assignment when these outputs are required.

## Versions and synchronization

Use independent directories or version control as appropriate, for example:

```text
project/
  brief.json
  variants/A/v2/{build_model.py, model.blend, model.glb, checks.json}
  variants/B/v4/{build_model.py, model.blend, model.glb, checks.json}
  renders/brochure-01/
```

Record `parent_version`, change scope, source hashes, confirmed values, and unresolved items per version. Preserve the parent when deriving a variant. Explicit synchronization permits updates to specified variants while retaining a recoverable state.

List shared modules and variant differences before synchronization. For example, A has a round window and B a rounded rectangle, while ceiling, furniture, floor, and rear-wall control screen are shared. Shared-interior updates still require front lining adapted to each opening; copying an entire panel can create mismatched window cutouts.

Preservation checks compare actual geometry, world transforms, topology, material assignment, and textures, allowing reasonable tolerances for tiny floating-point differences. A file hash proves that a whole file was not rewritten; it does not prove equivalence of components inside different files.

## Viewers and delivery models

Export GLB for interactive review and retain native files/modeling source for further editing. Decide whether OBJ, STEP, or another format is needed from its use; do not present a mesh format as manufacturable parametric CAD.

Check texture paths, scale, viewing direction, clipping, and door movement. Clearly identify section, normal exterior, and interior viewer modes. Do not save a temporary inspection hide state as a product missing components.
