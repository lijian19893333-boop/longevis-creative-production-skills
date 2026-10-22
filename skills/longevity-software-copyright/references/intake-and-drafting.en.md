# Intake and drafting

## Compare the current template

Read the actual form before writing. List every label, input location, instructions and length limit. If the form has 30 fields, check all 30; do not substitute an unrelated standard form. A legacy `.doc` may need conversion with an available office tool. Keep the original, verify the converted layout and avoid renaming a DOCX to `.doc`.

The [blank working record](../templates/intake.blank.json) groups common information; fields vary by agency and filing system. Record a value, status and source for each fact. Status vocabulary: `confirmed` (owner confirmed), `observed` (visible evidence), `documented` (stated in an identified document), `proposed` (draft suggestion), `pending` (unknown). Status is about the fact, not final filing approval.

| Area | What to establish |
|---|---|
| Identity | Official owner, identity evidence and ownership/development basis |
| Software | Full/short name, version, category and exact application boundary |
| Dates | Actual completion, publication status, date/place evidence; proposals visibly marked |
| Environment | Actual hardware/OS, development tools, runtime and programming languages |
| Source | Version, own-source scope, original line count, native projects and exclusions |
| Function | Purpose, users/industry, main modules, workflow and supported characteristics |
| Contact/signature | Authorized recipient/contact and who supplies final signature/confirmation |

Do not infer independent development or sole ownership from a company name. Commissioned/cooperative development, licensed modifications and transfers may require additional evidence. Flag a question; do not invent an agreement or signature.

## Main-functions narrative

If the drafter requests at least 500 Chinese characters, draft enough relevant material to survive edits and count Han characters, excluding punctuation, Latin identifiers and numbers. Keep that requirement attached to its source. Run:

```sh
python3 scripts/check_function_text.py main-functions.txt --min-cjk 500
```

Commands are relative to this skill's directory; the text can be anywhere. The counter checks length, not quality, ownership or implementation. Do not add generic filler solely to reach the target.

Build the narrative from supported facts: users and purpose; input/settings; principal modules; normal workflow; observable outputs; stored records; exceptions and recovery; supported technical distinctions. State whether a function exists in code, only in requirements or remains unverified. No treatment efficacy, arbitrary pressure/temperature ranges, algorithm claims, cloud features or security functions without project evidence.

## Operation manual

Use the current version's own screens: prerequisites, startup/login if present, main screen, settings, normal operation, status/termination, records and common failures. Each step states the starting state, user action, displayed result and supported recovery. Include only relevant modules. Keep captions, controls, units and screen names consistent with the application.

Prefer actual authorized captures. If only historical screens or a design preview exist, label them and state the version limitation. A generated illustration can explain a concept but cannot prove runtime behavior. No fabricated screenshot is acceptable as an actual software capture.

## Design description

Explain actual architecture, module responsibilities, state flow, data structures/storage, interfaces, validation, errors and persistence. Clearly distinguish UI commands, communication ACK and real controller feedback. Do not import another product's production protocol, secret maintenance password or parameter limits. HMI screen configuration and event scripts may be documented alongside their native export rather than misrepresented as a conventional text-only application.

## Cross-document checks

Check official name/version, owner, dates/status, language/environment, source count, module names, data fields and supported capabilities across every file. Keep one canonical facts register. Copying another product's completed form is a starting convenience only; remove all carried-over facts. A drafter may request both operation and design documents, while ordinary filing rules refer to a qualifying documentation material; do not imply both are universally mandatory.
