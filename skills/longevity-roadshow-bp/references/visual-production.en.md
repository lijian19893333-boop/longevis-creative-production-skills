# Images, Integration, and Editable Delivery

[中文版](visual-production.md)

## Set direction from the industry's experience

Identify actions, settings, and wearing details familiar to the audience. In golf and similar sports, credibility comes from correct grip, swing, hitting positions, fairways, coaching relationships, and equipment scale rather than decorative balls, flags, and blue circuitry.

Express technology through precision structure, materials, lighting, measurement information, and product interfaces. Express fashion through clothing proportions, materials, styling, and photography. Both should relate to the same real product.

## Two visual organization options

| Direction | Suitable content | Execution |
| --- | --- | --- |
| Clean editorial | Dense information and a brand that emphasizes simplicity | Rhythmic whitespace, clear type hierarchy, a few distinct hero images, native charts |
| Integrated scenes | Experience, brand, product, and channels requiring a sense of place | Full-bleed or large real scenes, text-safe areas, natural product/environment transitions |

The same main deck can combine both within one brand system. Do not crowd every slide merely to demonstrate a background, or reduce all business slides to the same plain-colored template.

Continue an established preference directly. Multiple proposals help choose a direction; comparison pages do not automatically belong in the roadshow deck.

## Plan image assets

Assign images before generating them. Each content image has one purpose and one slide in the main deck. Deduplicate backgrounds and content imagery together; register logos, headers, and generic small icons separately.

Useful image scales include overhead scenes, full figures, action close-ups, equipment details, material macros, structural exploded views, interface experiences, and packaging/delivery details.

Recropping one coach, recoloring one belt, or placing different gradients on one lawn does not create an independent image. Even a generated new angle needs review for being only a minor variation of the same composition.

Generation prompts should specify:

1. The slide and topic the image supports.
2. Subject, action, scene, and shot scale.
3. Subject placement and whitespace required for text.
4. Materials, lighting, and the project's grading baseline.
5. Product and human-action details that must remain correct.
6. No slide titles, fabricated data, third-party marks, or full-page PPT images containing UI.

Save the exact prompt, input references, generation mode, output file, and slide number. Copy all project assets into the project directory rather than relying only on a tool's default output folder.

## Product design consistency

Select one design baseline and record silhouette, dimensional constraints, CMF, mechanical relationships, concealed electronics compartment, wearing method, and branding position. Apply it to heroes, wearing shots, exploded views, website imagery, and devices shown in the app.

Separate engineering parameters from design proposals. Appearance images cannot prove waterproofing, precision, battery life, mass production, or certification. A conceptual exploded view must not be presented as completed engineering validation.

## Natural integration

Use transparent assets or hero images composed specifically for the slide. Align light direction, perspective, color temperature, contact shadows, and sharpness so product edges feel natural.

Do not paste an entire reference page onto a new background or retain rectangular white backgrounds around products. If blurring white edges still leaves the subject floating, redo the light/shadow or composition.

Keep text areas calm. Dense architectural lights, metal reflections, bunkers, sunset water, wrapping paper, and lawn highlights can undermine body-text contrast. Native masks can adjust exposure, but must not make the image nearly invisible.

## App / website

Interfaces must match product commitments. Organize them around real user actions such as connection/calibration, recording, comparison, and review, according to actual project functions.

Label unmeasured values in UI imagery as examples. Do not imply support for unconfirmed automatic recognition, full-body capture, disease diagnosis, or performance improvement.

Keep key copy, data charts, and explanations as native PPT objects. Device frames and complex product renders may be images. Avoid meaningless cards and buttons added merely to appear “interactive.”

## Editability and export

Follow the current presentation skill. Discover tool versions and runtime paths from the environment; do not make one task's absolute path a permanent dependency.

- Keep text, tables, charts, and necessary structural diagrams native in PPTX. Data charts need usable workbook bindings.
- For background-only replacement, prefer minimal edits to image relationships and necessary masks while preserving native content. Import/re-export can alter chart bindings; inspect actual package structure.
- OOXML image targets may be relative or begin with `/ppt/...`. Resolve them before comparing media hashes; filenames alone are insufficient.
- Prefer vector/text PDF output. If the current engine genuinely cannot export PDF, render the final PPT slide by slide at high resolution into a static PDF preview. State that it is a preview and retain PPTX as the editable source.
- Derive the PDF preview from the final PPT, never a mixture of old and new renders.

## Boundaries of the image-deduplication helper

`scripts/audit_pptx.py` uses only Python's standard library. It hashes image contents with SHA-256 for images actually referenced by slides. Identical bytes across slides are reported even under different media names.

It also reports missing image references, native table/chart counts, slides containing charts, and embedded workbook counts. Exit code 0 means these checks found no issue; exit code 2 indicates reused/missing images requiring human handling.

It cannot judge image themes, correct motion, product consistency, approximate reuse after cropping/grading, text within images, or layout aesthetics. A full contact sheet and visual inspection of every slide at its intended size remain required.
