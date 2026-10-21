# Rendering and Delivery

[中文版](rendering-and-delivery.md)

## Shot design

Reference shots include front-left hero, front, front-right, open door, interior overview, furniture/equipment, ceiling lighting, and handle/material close-up. Remove or replace shots to suit the product; do not repeat nearly identical compositions just to reach a count.

Keep the source model at real scale and compose through camera position and focal length. For front comparisons, use long-lens perspective or appropriate orthographic views, avoiding base cropping. Horizontal orthographic rays near the image bottom may originate below ground and produce a gray strip; use long-lens perspective or adjust camera height.

A light warm-gray studio can use a continuous curved backdrop and soft area lights. Separate white products from the background, preserve contact shadows, and avoid clipped white metal highlights. Do not impose light gray on other users.

For interiors, temporarily hide front occlusion in the render scene if necessary, but crop away shell cross-sections and exposed structural edges. Check all four edges for accidental control-screen fragments, furniture corners, or fixture edges. Keep star-ceiling points crisp instead of masking geometry with excessive bloom.

## From proof to final render

- Start with approximately 600–1000 px proofs covering representative exteriors, interiors, and complex transparent parts.
- Render one image at final resolution, inspect it enlarged, and record duration. Low-resolution runtime is not a direct estimate for the full batch.
- The example uses Cycles, denoising, and adaptive sampling. 64 samples is a starting point, not a quality guarantee. Increase selectively for noise, transparent parts, or unstable small lights; do not blindly set extreme samples for every shot.
- Inspect available GPUs before choosing the backend; use CPU explicitly when no compatible GPU exists. Sequential rendering in one GPU batch is often easier to control; competing processes may not improve speed.
- Write each file and completion record separately. An old PNG after interruption does not prove success. Validate a new temporary output before replacing the target and recording its hash.
- After camera, material, model, or recipe changes, use configuration fingerprints to decide rerenders. Do not fabricate completion records. Record sources of reused images too.

## Transparent parts

Low Alpha used for web glTF visibility can combine poorly with Cycles transmission, creating ghosting or implausible transparency. Assess Alpha, Transmission, IOR, and Roughness only in the render copy. Retain actual panel thickness and material requirements. Do not remove the door or treat polycarbonate as air to obtain a clear image.

## Images and checks

Brochure images can start with a 3000–4000 px long edge, determined by layout, cropping, and print size. The example used 3600×3000 exteriors, 3600×2700 interiors, and 2400×3600 close-ups; scripts do not fix these dimensions.

Provide text-free PNG and high-quality JPG. Overviews may carry variant/shot labels but remain separate from individual layout images.

`print_mm = pixels / dpi × 25.4`. At 300 dpi, 3600 px equals 304.8 mm. Changing dpi alone does not make a low-pixel image high resolution. Preserve sRGB ICC; CMYK conversion must match printer, paper, and output conditions.

Final checks: every image opens; pixels and ICC match claims; variant/shot counts agree; hashes are valid; ZIP CRC passes; source models are unchanged. Use overviews for composition/color, then enlarge glass, metal, seams, and lettering. Script checks do not replace visual inspection.
