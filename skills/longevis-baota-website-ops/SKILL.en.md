---
name: longevis-baota-website-ops
description: Use when uploading, updating, publishing, migrating, or rolling back websites on Baota, self-hosted servers, Nginx, systemd, or PM2, including ambiguous static versus SSR artifacts or uncertain deployment status.
---

# Baota and Self-Hosted Website Deployment

[简体中文](SKILL.zh-CN.md)

Treat each release as a verifiable, recoverable version switch. Discover the project's actual build and runtime before deciding what to upload. Panel registration, a running process, internal health, and a working public domain are different evidence.

## Before starting

Record the target site, environment, domains, source revision, build scripts and artifacts, production directory, runtime entrypoint, process manager, bind address/port, database/private media/env/configuration, and rollback point. Read the current project's README, package manager lockfile, scripts, and deployment documentation. Do not infer paths, ports, Node versions, commands, or accounts from this skill or old records.

Preserve the user's existing authorization scope. When release authorization and targets are clear, complete backups and candidate checks, then proceed with the switch without asking for the same authorization again. Pause dependent actions only for an unknown critical target, an action outside authorization, or a tool-required approval; continue independent preparation. This skill itself does not authorize production operations.

## Deployment decisions

| Observation | Decision |
| --- | --- |
| Project confirms static export with entry HTML in its build output | Serve static files with Nginx; identify API/admin services separately |
| Project confirms SSR/Node execution with its matching entrypoint | Deploy runtime files, dependencies, and service according to the project contract; reverse proxy with Nginx |
| Multiple outputs such as `dist/` and `.output/` coexist | Inspect scripts, README, and the actual production entrypoint; rule out stale artifacts instead of guessing from folders |
| Expected output is missing or the startup contract conflicts | Repair the build/configuration before deployment |

`dist/index.html` and `.output/server/index.mjs` are common examples, not universal standards. Other frameworks require project-specific evidence.

## Execution constraints

1. Classify by the highest impact. Text/images can use an existing admin draft and preview flow. Changes to API, database, env, permissions, services, domains, or DNS require the complete affected application and configuration, not a frontend-only upload.
2. Run checks and builds that actually exist in the project, locally or in an isolated build environment. Package required runtime files and verify the manifest, size, and SHA-256. Include dependencies required by the runtime contract; do not blindly exclude every dependency directory.
3. Preserve the previous version and validate an independent candidate directory/test site. Back up the database, private media, env, and Nginx/service configuration; verify readable backups and recovery steps. Keep persistent state outside release directories and Web roots.
4. Assign one process manager to each service. Baota Node, systemd, and PM2 must not compete for one port. A manager migration must cover env, data, processes, traffic switching, and rollback.
5. After candidate checks, switch within existing authorization. Change domains/DNS only within scope. Verify public URLs, critical business flows, and recovery paths according to the actual impact.

See the [English runbook](references/deployment-runbook.en.md) for deployment, maintenance, and recovery procedures, or the equivalent [Chinese runbook](references/deployment-runbook.zh.md).

## Delivery evidence

Report source revision, build/package checks, candidate acceptance, backup locations, the actual process manager, public URL verification, known issues, and rollback point. Distinguish local/test-only results from checks performed in production. “Upload successful,” “running,” and “works locally” do not establish a completed public deployment.

Never put passwords, tokens, cookies, SMTP credentials, databases, or private media in chat, Git, public artifacts, or logs before redaction. This public version supplies a method, contains no site credentials, and does not establish that any particular site has been deployed.
