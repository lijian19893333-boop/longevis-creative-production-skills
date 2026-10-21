# Baota and Self-Hosted Deployment Runbook

[中文版](deployment-runbook.zh.md) · [Back to skill](../SKILL.en.md)

## 1. Establish targets and change scope

The site register should contain: release ID; environment and domains; source revision and working-tree status; build/start commands; actual artifacts; production/candidate/previous-release directories; runtime version and executable; service user; process manager; bind address/port; Nginx configuration; database, private media, env, and backup locations; switching and recovery steps; authorization scope; and verification owner. Record current verifiable facts and mark unknowns explicitly.

| Change | Release scope |
| --- | --- |
| Text, images, or ordering supported by an existing admin interface | Snapshot → draft → preview → publish → check public pages |
| Source, components, or synchronized content across pages | Update content sources → build → independent candidate → version switch |
| API, database, env, login/permissions, process manager, Nginx, or domains/DNS | Handle application, configuration, data migration, and recovery together |

Classify mixed requests by their highest impact. “Replace a homepage image and change the form API” is a full affected-application release. Do not overlook the backend because the first item is simple. For unknown critical targets, inspect configuration, project documentation, and current processes first; ask for missing essentials only if they cannot be established. Do not guess production paths.

## 2. Discover the build and runtime contract

Read the README, deployment documentation, package manager lockfile, scripts, framework configuration, existing Nginx rules, and process arguments. Establish build commands, output directory, static-export versus server execution mode, runtime dependencies, port/env sources, and health-check endpoint. Use the project's actual package manager and locked version; do not assume any particular `npm`/`pnpm` script exists.

Static output commonly includes `dist/index.html`; SSR may use `.output/server/index.mjs`. Folder names are clues only. If both exist, investigate stale builds and multiple targets; confirm results using a clean candidate workspace and an explicit build script. Other framework outputs follow their own contracts. Repair missing expected artifacts or inconsistent startup modes before upload.

A static frontend can still depend on API, forms, admin functions, databases, or email services. Inventory each dependency instead of classifying the whole site as static merely because entry HTML exists.

## 3. Build, package, and verify

Run existing, applicable type checks, tests, lint, builds, and business checks locally or in isolation. Record actual commands, results, and source revision. State unavailable checks rather than inventing passing results.

Include artifacts, required runtime dependencies, migration scripts, and sanitized configuration templates according to the runtime contract. Exclude real env files, credentials, databases, private media, backups, Git history, development caches, and unrelated source media. Some SSR runtimes require bundled dependencies or framework-traced output; verify project requirements instead of mechanically deleting `node_modules`.

The following example only verifies an existing archive; set the variable to the actual release file. It does not deploy anything:

```bash
release_archive='/absolute/path/to/release.tar.gz'
tar -tzf "$release_archive"
gzip -t "$release_archive"
shasum -a 256 "$release_archive"  # sha256sum is available on Linux
```

Inspect manifest paths and sensitive files, and record archive size and SHA-256. Recheck the digest on receipt before extraction into an independent candidate directory. Integrity checks establish transfer consistency, not runtime viability or absence of sensitive data.

## 4. Backups and persistent state

Preserve the previous release and back up databases, private media, content snapshots, env, Nginx, and the actual service configuration before deployment. Store backups in restricted, non-public locations. Use engine-appropriate consistent database backups: consider active writes/WAL for SQLite, and supported snapshot/export mechanisms for other engines. Verify readable backups and recovery steps in isolation; an existing file is not proof of successful recovery.

Keep mutable data, private media, and logs outside replaceable release directories. Sensitive state and backups must also stay outside Web roots. Grant only permissions required by the service user; do not use `chmod -R 777`. If state is inside an old release directory, prepare an independent persistent location and verify data consistency before scheduling the switch.

## 5. Environment, migrations, and process management

Store real env values only in restricted server files or a secure configuration interface; redact displayed logs. Candidates must not accidentally write to production targets or message real customers. Use test data or controlled tests within authorization.

Separate new-database initialization from existing-database upgrades. Inspect migration history, target, backup, and compatibility before using the project's migration mechanism; do not rerun unknown SQL manually. Record post-migration read/write checks and recovery conditions. For destructive migrations, establish whether the previous application can still read the new schema.

Choose one actual manager per service: Baota Node, systemd, or PM2. Registering a project must not start a duplicate process. Verify real bindings and the service user against configuration. Loopback binding is usual behind a local reverse proxy; containers or other network topologies must follow their verified network design.

A process-manager migration is a separate service change. Check env, working directory, runtime, persistent state, and health checks; prepare process/traffic switching order and rollback. Do not stop the only working service first and improvise its replacement configuration afterward.

Enable Nginx static fallback only for relevant frontend routes. API/admin/private-media paths require their own matching rules to avoid turning failed API calls into `200` HTML responses. Reverse proxy SSR according to the project. Run `nginx -t` after configuration changes and reload only on success. For systemd changes, daemon-reload when required, reload/restart the affected service, and inspect state/logs. Use PM2/Baota operations when they are the actual managers.

## 6. Candidate acceptance and switching

Validate the candidate using an independent directory, test domain, or controlled Host before replacing the only production directory. Check applicable project requirements:

- Homepage, core pages, deep links, 404, static assets, and expected version; both HTTP status and content must be correct.
- Backend health, database migrations, logs, and behavior after service restart.
- Form/API fields, success/failure, duplicate submissions, status codes, persistence/email, permissions, and rate limits. Use authorized safe test data and matching frontend/backend versions.
- Admin login, media draft/preview/publish/unpublish, public-access gates, and unauthorized-access behavior.
- Actual video playback and required Range requests; large assets, incorrect domains, temporary links, and third-party dependencies.
- HTTPS, canonical, robots, sitemap, and admin noindex; desktop and approximately 390px mobile layouts, plus target in-app browsers when relevant.

When candidate checks pass and production switching is already authorized, proceed without asking for that authorization again. Clarify out-of-scope DNS, domain, data-deletion, or other actions separately while continuing independent preparation. Use the project's verified version-pointer, configuration, or traffic-switch method. Atomicity of a link switch depends on filesystem and implementation; saying “atomic deployment” does not prove it.

## 7. Public production verification and evidence boundaries

After switching, recheck the production domain's TLS, intended version, key routes, API/forms, media, and logs. Internal health and a working test domain do not prove the public entrypoint is correct; caches/CDNs, DNS, or multiple origins may still serve an older release.

For domain changes, check authoritative DNS, target addresses, certificate hostname/actual certificate contents, HTTP responses, and page version. Explain edge and origin checks separately when a CDN/proxy is involved. Record incomplete propagation or unavailable external checks instead of claiming that every visitor has switched.

Record local-build success, candidate acceptance, switch execution, public-entrypoint verification, and complete business-flow verification separately. Leave missing evidence pending rather than upgrading its status.

## 8. Rollback

For blank pages, failed startup, API/database failures, mixed static assets, permission leaks, or TLS/Nginx faults, stop stacking changes and preserve logs/current version details. Follow the plan to point traffic/services to the previous release and restart affected services as needed. Restore databases through the verified engine/project procedure. Code rollback alone does not undo migrations; never improvise table deletion.

After recovery, recheck public pages, API/admin, media, permissions, and logs. Record cause, recovered version, time, data impact, and next repair. Clean up backups according to project retention policy; do not delete the only recovery copy before acceptance.

## 9. Release record template

```text
release_id / timestamp and timezone:
site / environment / domains / authorization scope:
change class / summary / impact:
source revision / working-tree status:
actual build commands / check results:
artifacts / archive size / manifest / SHA-256:
previous / candidate / current version:
backup locations and restore verification (no credentials/private content):
migrations / manager / ports / configuration actions:
candidate checks / production URLs and business-flow results:
unverified items / known issues:
rollback steps / data compatibility / rollback result (if executed):
```

This public runbook contains a general method, not production-site history, accounts, credentials, or actual deployment results. Each project's deployment documentation and release records maintain its actual commands and long-term facts.
