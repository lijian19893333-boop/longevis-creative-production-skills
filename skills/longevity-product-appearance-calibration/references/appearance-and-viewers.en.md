# Appearance and Viewer Behavior

[中文版](appearance-and-viewers.md)

## Material judgment

- **Coatings and bare metal:** Black coatings still need readable broad highlights. Determine whether an opaque coating covers the substrate before setting metallic; an industrial product does not imply metallic=1 everywhere.
- **Glass:** Assess both reflection and transmission. glTF alpha blending and `KHR_materials_transmission` are different mechanisms. Check actual renderer support and values after loading. Existing door code that reduces alpha with opening angle can undermine calibrated transmission.
- **Wood:** Fine grain depends on real-world scale, direction, roughness, and restrained normal amplitude. Keep broad base color credible. Different wood species or finishes cannot be established by tinting the same generic grain. AO should not turn every seam into a black line or bake in color from switchable lights.
- **Fabric and rubber:** Use microstructure, roughness, and limited sheen to describe fabric; preserve seams, grooves, membranes, and actual UVs. Rubber often scatters more than adjacent bare metal, but follow the reference and actual material.
- **UI and marks:** Preserve original textures. Avoid covering them with global recoloring or microtexture. Check screen-off and restored states.

## Assessing local colored light

For interiors with colored lighting, tune frame material, glass transmission, wood grain, and distributed lights separately. Remove implausible hotspots before deciding whether a low bounce approximation is needed. Approximate bounce lights are not physical measurements.

Check whether emitter colors remain readable, grain survives in lit areas, illumination varies with distance, shadows retain detail, glass combines interior visibility with edge reflections, and contact shadows meet the object. These are assessment criteria, not accurate colors or intensities transferable to another product.

## Asset and viewer integration

A static catalog may be enriched at runtime to load a different model. Dedicated pages may load separate closed/open/interior/floorplan assets, and download buttons may target another alias. Trace every actual URL through network requests rather than searching only for source filenames. This public package does not interpret arbitrary JavaScript, databases, or product catalogs.

Shared controls, device controllers, and dedicated viewers may override color, emission, and transparency after loading. If the model is correct but its display is wrong, inspect final material values. Adding `KHR_lights_punctual` requires controlling the actual lights: switching off emissive material does not switch off those lights. The helper's node extras `controlMaterial` and `appearanceLightGroup` are metadata only; the viewer must explicitly read and connect them to controls.

Check environment maps, tone mapping, exposure, shadows, units, and cache fingerprints. The native model and browser-loaded file may differ, and a browser screenshot does not validate a native render. Record renderer/version and the functions actually verified rather than assuming identical extension support across viewers.

## Native tools and asynchronous operations

Blender node socket names, compositor APIs, and GPU selection change with versions. Inspect the current interface before reusing old property names. When running Python through the CLI, use the supported `--python-exit-code 1` option so Python exceptions affect process status, and inspect logs. Exit status alone does not prove visual correctness.

Bind asynchronous export and model-change operations to the model that owns the task. When an old task finishes, restore only that model's dimensions, camera, and busy state. If the user switched models or the viewer was destroyed, discard stale restoration operations. Specifically test exporting a PNG and immediately switching configurations.
