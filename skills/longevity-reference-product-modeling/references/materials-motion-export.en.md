# Materials, Motion, and Export

## Materials and textures

Prefer official logo/UI sources over cropped renders; embedded high-resolution PDF images are the next option. Crop only the active display and rectify its four-corner perspective. Do not bake the bezel, duplicate reflections, or shadows into the texture. Preserve aspect ratio; an unconfirmed “similar blue interface” must not replace a purple original.

Use sRGB for color textures and Non-Color for normal/roughness data. Avoid coplanar flicker or occlusion between display, glass, and door. Inspect surface positions and UVs before introducing any necessary small offset. Grilles need appropriate relief/thickness; a black-line texture cannot replace a physical slot required in close-up.

For metal highlights, distinguish geometry, smooth normals, and lighting. Adjust one variable class at a time and inspect front and oblique views. Do not damage the overall color to brighten one region. Appearance-matching light/emission compensation is separate from actual engineering illumination specifications.

Recheck flat-face normals and UVs after bevel/Boolean topology changes; incorrectly smoothed triangle fans can create star patterns. Meshes using normal maps need valid tangents; do not dismiss every exporter warning. Preserve per-face material indices when recoloring multi-material objects. Darkening exterior panels must not also darken white internal lining.

## Doors and disassembly

Create a real hinge parent and preserve world transforms while parenting the door panel, handle, seals, and door-mounted display. Keep fixed glass, shell, walls, and floor in fixed collections. Inspect closed, intermediate, fully open, and reverse-closing states for axis errors, sweep collisions, wall penetration, and detached parts.

Multiple doors need independent states. If a viewer can play only one animation at once, export combinations such as “door A moves while B remains closed/open” to prevent animation changes from resetting the other door. Root-node names and opening angles come from the current model, rather than hard-coded inherited examples.

Opening, hiding parts, sectioning, and exploded views are different functions. Do not simulate opening by making the entire cabinet transparent. Preserve/restorable original component transforms for disassembly. Click-to-hide needs clear selection and restoration controls; “open door” must not delete a wall.

## Files

Blender: save real geometry, semantic components, meter/millimeter conversions, packed textures, and reproducible source. GLB: inspect axes, animation, materials, normals, and embedded images. The basic viewer expects ordinary GLB without extra decoders. Never overwrite the only source with decimation or conversion.

STEP is not merely another export format for a render mesh. Engineering handoff usually needs sensible solid parts, assembly relationships, clean analytic surfaces, and accurate dimensions. Converting every Blender triangle into BRep can produce huge, inefficient files. If SolidWorks-compatible delivery is separately requested, prefer existing solid CAD; build solids by actual parts and validate solids, units, and import. Explain that STEP generally does not preserve native feature history or every assembly mate. An appearance-model request alone does not call for engineering reconstruction.
