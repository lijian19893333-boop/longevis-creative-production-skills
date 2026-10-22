# Source materials and local helpers

## Establish the actual application boundary

Identify the program before selecting pages. Record the source revision, application name/version, entrypoints, modules, languages, developer/ownership evidence and separately maintained controller firmware. Inspect build files and routes. If a build is available, check its version against source and screenshots without silently altering it. A successful APK build does not establish installation, hardware communication or complete-machine acceptance.

Review and document the inclusion order. Include the relevant own program, including necessary owned UI resources or embedded logic; exclude third-party/generated/test/demo files only with a reason. Alphabetical order can be reproducible but is not proof of correct program structure. Vendor source is not automatically owned source. Do not exclude inconvenient own modules to improve the page count.

For graphical HMI platforms such as McgsPro, retain the native project and hash. Export screens, objects/configuration, events, scripts and relevant logic with the platform where possible. Binary string recovery is a partial extraction unless coverage is demonstrated. Record offsets/record IDs and methods, and distinguish configuration from scripts. Text fragments cannot prove all native logic has been recovered. A native `.MCP` is deliberately inventory-only in the helper.

## Run the helper

Requires Python 3.10+ and the standard library. Commands are relative to this skill directory. Work on a copy or frozen revision. Create `files.txt` with one reviewed relative source path per line, in the intended order. No glob expansion or automatic folder ingestion occurs. Example (synthetic names):

```text
app/src/main/java/example/MainActivity.kt
app/src/main/java/example/SessionState.kt
```

```sh
python3 scripts/source_materials.py inventory ./project-copy --files ./files.txt --out ./work/source-manifest.json
python3 scripts/source_materials.py extract ./project-copy --manifest ./work/source-manifest.json --out-dir ./work/material-v1 --name "Example control software" --version "V1.0"
```

Keep outputs outside the source root. Existing manifests and output directories are not overwritten. UTF-8 decoding is strict; use `inventory --encoding gb18030` or another verified encoding when appropriate. Do not use replacement decoding that loses characters. Symlinks, duplicate paths and paths outside the root are rejected. File-list order is preserved. The helper does not discover omitted files or detect every secret; review the list and text yourself.

`inventory` records relative paths, SHA-256, bytes and physical/nonempty line counts. Native/binary files can be hashed but cannot be rendered as program text. `extract` rechecks hashes before writing, omits blank-only lines, preserves all retained characters including comments, and emits:

| File | Purpose |
|---|---|
| `selected-source.txt` | Original selected nonempty lines; no added file labels or page fillers |
| `pages.json` | Logical page and row → relative file, original physical line and global nonempty-line number |
| `source-manifest.json` | Copied inventory, encoding and hashes |
| `review.json` | Count, selection mode, name/version and unresolved review status |

Default settings: 50 lines per logical page, 30 pages from each end. At most 3,000 nonempty lines: select all. More: select the first 1,500 and last 1,500, without overlap. `--lines-per-page` and `--side-pages` configure a different confirmed requirement. These are formatting choices, not a legal definition of source lines. The last page of a short complete program stays short; no padding. A whole short program and a short partial extraction are different cases.

The helper always reports `scope_status: unreviewed`; successful hashes establish only that listed files match the inventory. Preserve separate human evidence of complete scope, ownership and reasons for exclusions. It does not create Word/PDF, export a proprietary HMI project, parse source semantics, certify ownership or submit an application.

## Format and verify

Use `pages.json` for deliberate page breaks and exact name/version headers in the authoring tool. File labels, headers and line numbers are metadata, not original source lines. Preserve the complete program order in the working archive and identify the omitted middle range in the extraction note. Render the PDF, check every page and compare source text line by line with `selected-source.txt`, allowing only documented layout normalization. Check long-line wrapping, tabs, Chinese glyphs, first/last lines and the final program boundary. Overflow pages are not more source.

If source is missing, continue supported form/manual work and add a precise gap note identifying the version, source/export/build needed and why. Do not draft plausible application code to conceal missing evidence. Building or modifying software is a separate user request.

Tests use synthetic files only:

```sh
python3 scripts/test_helpers.py
```
