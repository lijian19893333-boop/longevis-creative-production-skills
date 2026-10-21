---
name: longevis-website-launch
description: Use when launching or maintaining a website, optimizing media delivery, deploying to Baota/ECS, switching domains or HTTPS, or verifying SEO/GEO readiness.
---

# LONGEVIS Website Launch and Maintenance

[中文版](SKILL.md)

Turn a locally approved site into an accessible, maintainable, recoverable production website and report actual release evidence. This public version retains reusable methods without real servers, accounts, domain configuration, or historical deployment records. Verify runtime configuration in the current environment.

## Choose the working mode first

- **Summarize or organize a skill:** read records, extract procedures, and produce documentation. This request does not authorize production, DNS, database, or external-account operations.
- **Update or release a website:** identify the correct project and currently running version, then execute according to scope. Existing authorization remains valid. Ask again only when an actual action exceeds it or an explicit project requirement remains unmet, after preparing a previewable, reviewable result.
- **Single maintenance task:** perform only relevant stages. Replacing text or adjusting mobile consultation access does not require repeating domain switching or database migration.

## Locate the project and evidence

Establish whether the user means a complete website, a standalone homepage preview, or an interactive workbench. Locate actual source, entrypoints, and release records. Read current `AGENTS.md`, `package.json`, changelog, and the relevant final release record.

Label historical summaries, old plans, and current runtime separately. When reconstructing history, final records identifying actual execution time, release identity, and read-back results supersede earlier “in progress/blocked” summaries. For current state, inspect the environment again. A newer-dated plan without execution evidence cannot override accepted deployment status.

## Execute as needed

See the [Launch runbook](references/launch-runbook.en.md) for execution and acceptance detail:

1. **Identity and scope:** record source project, running version, target domains, changes, data boundaries, and existing authorization.
2. **Homepage and content:** integrate the approved homepage into the complete website, preserving in-scope navigation, products, content, contact access, and administration. Follow current project rules for product identity and factual basis.
3. **Media and constrained networks:** show a clear poster first and load by visible scene. Preserve masters and make Web copies at approved quality. Distinguish download, decode, playback, and CDN status through measurement.
4. **Local and isolated acceptance:** run project checks and target build; verify desktop/390px layouts. Validate candidates with independent directories, ports, databases, and private-media copies.
5. **Baota/ECS deployment:** discover static versus SSR routing from the current project and follow the runbook. Back up, verify package hashes/release identity, switch services/static assets, and retain production state and rollback points.
6. **Domains and HTTPS:** where switching is required, separately verify DNS, target IP, certificate, redirects, canonical, and public page version. Baota and DNS administration have different responsibilities.
7. **Post-launch work:** check video, sound, contact access on both layouts, admin permissions, image chains, and SEO/GEO discovery. Gather separate evidence for indexing, ranking, and AI citation.

For retrospectives, use records of the user-specified project. Do not copy another project's IP, version, directory, counts, or rollback commands.

## Delivery contract

Complete and save acceptance records according to actual scope, using the [release record template](references/release-record.example.en.md) if useful:

| Field | Required explanation |
| --- | --- |
| Scope and identity | Changes; relationship between source/candidate/production versions; domain and actual runtime directory |
| Status | Separate progress for local checks, staging, switching, public verification, and search feedback |
| Verification | Time, desktop/390px, check commands/results, critical resources and business interactions |
| Data and rollback | Whether production data changed; backup locations; version-specific rollback and limitations |
| Pending work | Only actual unresolved items and next steps; old passing checks cannot substitute for a current failure |

Update project `CHANGELOG.md` and relevant acceptance records. Exclude passwords, private keys, sessions, and customer inquiries from skills, public reports, and delivery packages. Lead the final response with results and accessible entrypoints, then checks and pending work.

## Common misreadings

- Preview, staged upload, service startup, and production availability are different states. A platform success response still requires checking the user's actual URL.
- Verify data/media paths separately for each hosting environment. Deploying code must not silently import a demo database or reset live content.
- Gather separate evidence for CDN configuration, playable video, and improved first frames on constrained networks. File-download time is not every visitor's startup time.
- A configured 308 does not prove old-domain DNS resolves. HTTPS 200 does not prove the new server or the intended certificate is in use.
- Analytics script/beacon success, visible consultation greeting, and per-message auto-replies are three distinct acceptance checks.
- Explain sitemap-count drops, such as draft/obsolete-translation removal. Passing site-resource checks does not establish Baidu indexing or citation by domestic AI services.
