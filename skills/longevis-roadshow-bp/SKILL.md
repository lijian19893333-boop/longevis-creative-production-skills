---
name: longevis-roadshow-bp
description: Use when creating or redesigning an investor roadshow BP or financing pitch deck, especially from an existing deck whose substance must survive a redesign. Applies to investor narratives and visual production, not ordinary sales decks, training slides or product PRDs.
---

# LONGEVIS Investor Pitch Deck Production

[简体中文](SKILL.zh-CN.md)

Turn raw material into an investor-readable pitch deck that the team can continue editing. Establish the investment logic and facts first, develop the visual and image system, then inspect and deliver every slide.

## Scope and default preferences

- Use for new fundraising decks or redesigns that preserve an existing deck's substantive information.
- Current user instructions, approved direction, brand material, and slide-count requirements take precedence. Continue within existing explicit authorization instead of requesting approval of the same direction again.
- **Place fundraising on the last slide by default.** Do not automatically append thanks, original-text comparisons, source registers, design comparisons, or production reports.
- **Use every content image only once, including backgrounds.** A coach photo, product hero, or scene background cannot repeat across slides; cropping, flipping, grading, or masking still uses the same image. Logos, consistent headers, and generic small UI icons may recur as brand elements.
- Preserving substance does not require preserving the original slide count or poor layout. Move permitted redundant material out of the main deck and keep traceability records in the working directory.
- This skill does not prescribe an industry, palette, product, 19-slide structure, or historical funding figures.

## 1. Establish the project and scope of references

From the current conversation and materials, confirm audience, purpose, official brand spelling, output formats, fixed slide count, adjustable scope, and accepted/rejected elements. Ask only about genuinely missing information that affects the result.

Break references into independent elements: product shape, materials, exploded views, people, scenes, backgrounds, UI, type, and layout. Approval of an exploded view does not approve that slide's background or layout. Approval of UI quality does not import the example's functions or data.

An investor version still needs to explain business judgments. A request for something “ready to send to a product manager” usually means a complete handoff file; it does not turn the BP into a PRD.

## 2. Extract facts and track where content goes

Before redesign, inspect all text, images, tables, charts, footnotes, and notes in the existing deck. Maintain a working register:

`Original slide/information → destination slide → keep/merge/to fill → fact status → source`

- Treat confirmed facts, unverified user statements, public sources, planned targets, calculation assumptions, and design examples separately.
- Where team, R&D, users, partners, orders, deliveries, revenue, or cost lack evidence, retain editable placeholders.
- Preserve dates, currency, tax basis, denominator, and calculation conditions alongside numbers. Market installed base, annual revenue, and forecast sales are different measures.
- Simplify expression without removing qualifications material to a decision. Do not present targets as accomplished results.

For market, competitor, or funding calculations, read [Business narrative and facts](references/story-and-facts.en.md).

## 3. Order the investment logic before choosing slide count

Use the following logical order, merging by information density rather than assigning one slide to every item:

1. Brand and project positioning
2. Target users, real situations, and problems
3. Product solution and core value
4. Product form, key technology, or mechanism
5. Experience, app/service, and evidence of value
6. Market size and initial entry segment
7. Alternatives and differentiation
8. Charging, cost, and business model
9. Channel entry and customer validation
10. Team and actual progress
11. Milestones, key risks, and funding allocation
12. Funding request, use of proceeds, and corresponding outcomes

Follow the agreed slide count. If none exists, start with a compact main deck, usually 12–16 slides, and adjust for actual content. Preserving substantive information is a constraint; adding comparison pages and process logs is not a solution to overflow.

For each slide, write “What does this help the investor judge?” before arranging title, key evidence, supporting text, and images. Titles should name the topic or a conclusion supported by evidence.

## 4. Establish visuals and a slide-by-slide image plan

Define the project's visual character first. Premium sports wearables might combine real sporting scenes, fashion, precision hardware, and digital experience. Medical, industrial, or enterprise products should follow their own product and audience.

Create an asset plan before batch production:

`Slide | decision supported | image topic | camera/scale | unique asset ID | purpose | source/generation prompt | text-safe area`

- Assign each content image to one slide only. If assets are insufficient, generate/find different scenes and camera views or use native charts; do not reuse a crop of the same image.
- The same product may appear in independently composed wearing, structural, side, or material-close-up images if their visual content differs and the product design remains consistent.
- Backgrounds should suggest the industry setting while keeping brightness/detail subordinate to reading. Assess both scene richness and text clarity.
- First create representative product, scene, UI, and data slides, then extend the approved direction. Design comparisons are for discussion, not automatic inclusion in the BP.

See [Images, integration, and editable delivery](references/visual-production.en.md) for visual and technical details. This public package contains no real project's commercial information or example imagery.

## 5. Produce an editable main deck

Use the presentation skill available in the environment. Use image generation/editing capabilities and the relevant image skill when images are needed, and the available PDF workflow for PDF export. This skill supplies content and aesthetic decisions; it does not replace tool execution or final-check requirements.

- Keep titles, body text, key tables, data charts, and necessary UI explanations natively editable.
- Treat product renders and photography as image assets. Do not replace editable slides with full-page screenshots or paste white-background references awkwardly onto scenes.
- Use one design baseline for product appearance, CMF, wearing method, structural diagrams, and product images inside UI. Separate design concepts from engineering-validation status.
- Preserve each external/generated image's source, exact prompt, and slide assignment. Generated imagery cannot prove partnerships, product performance, or completed progress.
- Export a new version with a recognizable filename and retain source files. For image-only requests, preserve unrelated text and native evidence where possible.

## 6. Inspect before delivery

### Content and structure

- All required information has a destination; key figures, totals, units, times, and footnotes agree.
- Slide count follows the agreement; fundraising closes the deck; the main deck contains no unrequested process pages.
- Placeholders remain templates; plans and examples have not been promoted to achievements.

### Visuals

- Generate a full contact sheet to inspect narrative rhythm, similar camera compositions, and reuse of hero images or backgrounds.
- Inspect every slide at its intended size for overflow, overlap, human poses, product consistency, crops, and sharpness.
- Pay special attention to text contrast over bunkers, reflective metal, sunset water, packaging paper, and other highlights; adjust local masks or exposure if needed.
- Renaming the same image does not pass deduplication. Hashes cannot identify all cropped/graded reuse; visual review remains necessary.

### Files

Verify that the actual exported PPTX opens, native tables/charts and embedded workbooks exist, and the PDF page count and appearance match the final PPTX. Claim only checks actually completed.

Run the read-only helper to find cross-slide image reuse and missing image references:

```bash
python3 scripts/audit_pptx.py /path/to/final.pptx --report /private/work/pptx-audit.json
```

For individually confirmed logos or generic icons, add `--allow-reuse-media ppt/media/logo.png`. Do not exempt all unidentified media, content heroes, or backgrounds.

Default delivery: editable PPTX, PDF preview, full-deck overview, and independent assets/prompts. Keep audit reports in the working directory rather than appending them to investor material. Download links must point to verified final files.
