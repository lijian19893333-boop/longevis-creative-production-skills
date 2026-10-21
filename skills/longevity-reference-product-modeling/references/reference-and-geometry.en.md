# References and Geometry

## Minimum modeling record

Keep a short `MODEL_BRIEF.md` in the project, recording:

- Current objective and version; chosen layout and deliverable variants; what to retain, replace, or defer.
- Reference index: file/page, viewpoint, door state, layout, color, and components it establishes.
- Dimension table: component, value/unit, source, and confirmed/fitted status. Distinguish overall assembly from one cabinet, and state whether casters, displays, or transition spaces are included.
- World coordinates, forward direction, floor, main assembly datum, and Blender meter/millimeter conversion.
- Parts and connections: fixed/moving, parents, hinges, shared boundaries, and permitted CAD reuse.
- Inspection views and largest current differences.

Update the record when the user corrects a fact; do not preserve an earlier mistake as a permanent constraint. Ordinary image fitting can proceed autonomously. Clarify only consequential ambiguities that change the result.

## Read the reference

Check embedded image resolution in PDFs. Use original images rather than enlarging screenshots repeatedly. Crop multi-view boards by viewpoint while preserving the source page and crop coordinates. Covers, dimension arrows, and background display stands do not automatically become model components.

Image count does not equal geometric coverage: six perspectives of the same side do not establish the rear. A front image constrains that projection strongly; distinct directions, dimensions, and open-door views gradually establish three-dimensional relationships. Without rear evidence, produce the verifiable appearance and label the rest fitted or awaiting references.

Identify configuration differences using the relationship between viewing face, entrance, and equipment operating face, rather than screen-left versus screen-right. If a cabinet is behind the main body and its operating face is rotated 90 degrees, make a separate layout instead of mirroring the entire model. Use material configurations for color changes rather than offset duplicate geometry.

## Scale and cameras

Prefer annotated dimensions and user-confirmed values. Without a known scale, build relative proportions and label scale unresolved. For a known display diagonal and aspect ratio, calculate the active display's width and height before adding its bezel; enclosure width is not the display diagonal.

Orthographic views use one global scale and anchors such as the floor, center axis, or rear plane. For perspective references, establish projection and camera before judging depth; do not stretch axes independently to force a match. Exclude incorrect lens and camera direction before changing silhouettes.

## Shared cross-sections first

Use the top view to define inner/outer contours, clear space, and door opening; use side views for tilt and changes along height; constrain width and feature placement with the front view. Give shell, floor, and door frame shared boundary parameters. Independently improvised boxes produce gaps.

Define inner and outer surfaces separately. A protruding display on the exterior door does not imply an interior protrusion into standing space. Curved sidewalls do not imply a curved central panel; tilting a flat panel is a rotation rather than lateral curvature. Floors that should close a volume need actual faces. A lifting platform and fixed floor are different parts; use documented or confirmed gaps.

## Reuse CAD

List the allowed parts and check units, orientation, and assembly origins. Inspect imported equipment independently before combining it with the new exterior. Remove the old door, front frame, and duplicate chassis from a working copy. Check for old hidden objects occupying cavities and reversed interfaces. A plausible overall bounding box does not establish correct reuse of internal parts.

Organize components by actual assembly purpose. Several modeling operations on one continuous door panel do not make each face or small fragment a separate engineering part. Set decorative, hole-array, and grille density according to the final visible scale while preserving shape and physical layers.
