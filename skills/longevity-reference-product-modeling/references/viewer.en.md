# Local Interactive 3D Preview

Reuse a working project viewer instead of adding a page and port on each iteration. For a new project copy this skill's entire `assets/viewer/` into the project's `preview/`, put an ordinary GLB with embedded textures at `preview/model.glb`, and preserve `vendor/` intact. `index.html` provides the default English interface; `index.zh-CN.html` provides Chinese. Both have a language switch. `index.en.html` remains an English compatibility entry.

Run from the skill directory, substituting your actual preview directory:

```sh
python3 scripts/serve_viewer.py --directory ./example-project/preview
```

On Windows use `py` or the available Python command. The script prints the actual `http://127.0.0.1:PORT/index.html`; keep its process running. The link stops working when the process exits. For a stable entry point use `--port PORT` with a known available port. Do not kill an unknown process to resolve a conflict. Open `index.zh-CN.html` at the same host/port for the Chinese interface.

A localhost link works only on the computer running the server. To share, package the GLB, HTML, JS, and vendor directory so the recipient can serve them locally; sending your 127.0.0.1 URL is insufficient. The page can also select a local GLB without uploading it to a third party.

## Template scope

- Drag to rotate and zoom; six directional views, reset, and auto-rotation.
- List model-provided animations; play/pause and scrub the timeline.
- Refresh and load-error feedback; no fabricated “opening” when animations are absent.
- Bundled model-viewer 4.0.0 local module and upstream licenses; ordinary GLB needs no CDN script.
- No bundled Draco/Meshopt/KTX2 decoders. Supply actual dependencies for compressed models or export ordinary GLB first.

This is a basic viewer, not a complete CAD editor. Independent door buttons, part selection/hiding, sectioning, and exploded views require adaptation to the current product nodes/animations. An animation dropdown does not constitute full disassembly functionality.

## Actual pre-delivery checks

Check the server binding and loading of HTML/JS/GLB; see the actual model in a browser. Test views, rotation, animation middle/end frames, animation switching, refresh, and changing models. Exporting a new file does not prove the browser displays it; check filenames/hashes and cache behavior.

When the host supports a side panel, open the actual preview page there. If opening returns queued, report only that opening was requested. A tool screenshot or a static image alone does not satisfy an interactive-preview requirement.

The original helpers and documentation use the repository's MIT license. Bundled third-party code retains its own Apache-2.0, BSD-3-Clause, and MIT terms; see `assets/viewer/vendor/README.md` and accompanying license files.
