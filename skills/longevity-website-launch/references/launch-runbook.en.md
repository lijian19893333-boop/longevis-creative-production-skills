# Launch Runbook

[中文版](launch-runbook.md)

This runbook describes reusable steps, not production mutation commands to copy blindly. Tailor scope to the current project and authorization. Prefer sufficient connectors/APIs/CLIs for relevant services; use browser login and Baota interfaces when actually needed.

## 1. Identify the current state and this change

Create a short release record: project, current public version, target version, domains, build route, service working directory, static-asset directory, data/private-media locations, and backup/rollback point. Without a Git commit, identify the version by package SHA-256, manifest, key source hashes, and switching time.

Choose by task: content-only changes prefer existing CMS draft → preview → publish; source changes require build/candidate release; domain switches retain the accepted version/data; database migrations require separate target/authorization checks. Authorization to release does not imply a database reset or migration.

Baseline known public pages, contact access, admin permissions, and discovery entrypoints. Check for other unreleased workspace changes and include only this release's confirmed scope.

## 2. Homepage integration and fact checking

Integrate the approved homepage into the complete site, retaining navigation, footer, and existing routes. Verify mappings to actual products, models, 3D, and contact targets. Do not treat historical designs or engineering models as currently sold products.

Open 3D on demand. Pause scene video when its modal opens; after closing, restore according to the user's prior pause choice. Preserve both image proportions and readable text on mobile. Distinguish plain product images, scene imagery, and real project photography; do not stretch equipment images.

Use current confirmations/sources for specifications, delivery status, and awards separately. Keep missing models, returns, or performance unconfirmed. Project photos and organizers' award records must not become model certification or treatment-effect proof.

## 3. Media and constrained networks

Measure first: master size/codec, poster size, server bandwidth, Range responses, actual decoding, visible-scene requests, and failure fallbacks. Inspect first-screen behavior under controlled network conditions; smooth local playback does not rule out bandwidth bottlenecks.

- Make poster, text, and navigation usable first. Load active scenes or those near the viewport; do not prefetch all videos concurrently by default.
- Preserve masters. If quality requirements allow, produce compatible Web copies and verify composition, proportions, sharpness, audio, duration, and actual playback. Reduce resolution only within the user's confirmed scope. Without authorized quality reduction, start with scheduling, container faststart, caching, or controlled distribution.
- Automatic prefetch can stop offscreen. If the product requires user-initiated downloads to persist between scenes, distinguish manual and automatic tasks. Support visible progress, cancel/resume, and bounded concurrency. Do not extend that guarantee to page closure or separate-route navigation.
- Follow browser autoplay rules. If requested default sound is blocked, fall back to mute and show “Enable sound”; show “Mute” when audio actually plays. Explicit user mute/pause overrides asynchronous completion and scene changes.
- Verify public Range 206 and total length. Compare complete-file SHA-256 for the deployed transfer copy. Sampling segments only establishes access to those segments, not full-file identity or continuous playback.
- Mark CDN enabled only after configuration, usable media URLs, and successful request/playback tests. An inactive console or proposal remains pending configuration. Do not automatically buy or enable paid services.

## 4. Local and isolated server acceptance

Inspect current `package.json`, README, and deployment documentation to discover supported checks, target builds, startup, and audits. Do not assume particular scripts exist.

Publish static output only after confirming static-export intent and the matching entrypoint. For SSR, verify server entrypoint, Node runtime, and managed process; a development build does not replace the production target. When both outputs exist, follow scripts and the actual startup entrypoint. If dependencies are outside PATH, discover existing runtimes before reinstalling blindly.

Use an independent release directory and loopback-only candidate port, plus restricted copies of current production database/private media. Production copies remain private and must not be exposed, packaged, or delivered as test data. Mac dependencies cannot be deployed as native Linux dependencies; use accepted compatible dependencies or build in the target environment.

Inspect desktop/390px layout, homepage scenes, product/tool routes, contact access, and admin authentication. Report desktop 390px simulation separately from a physical phone. Site audits cover internal links, canonical, GET content types for original/optimized images, and protocol at every redirect hop. HTTPS images redirecting to HTTP count as failures. Explain page-count changes through publication state and translation versions before judging them.

## 5. Backup, switch, and rollback

Follow the actual process manager. Installed operational skills may help, but none is a required dependency of this runbook:

1. Back up consistent database snapshots, private media, env, Nginx/systemd, and relevant certificates. Verify readability/permissions and retain the old application directory.
2. Upload to an independent staging directory. Verify package SHA-256, manifest, target identity, and parent-directory permissions for public files. Successful staging still means only “uploaded.”
3. After candidate acceptance, switch production service and Nginx static root, syntax-test and reload. Avoid duplicate Baota Node/systemd port ownership. Read effective configuration, not merely one drop-in file.
4. Never replace production with a local demo database or seed automatically. Code rollback preserves data added since release by default. Restoring older data requires separate confirmation of target and time.
5. Compare new JS/CSS filenames, byte hashes, asset manifests, and real pages through public requests to detect stale long-lived caches. Retain assets needed by already-open older pages.

Prefer accepted builds generated from source. If a minimal runtime patch to server artifacts is actually necessary, verify exact prerequisite hashes, work on an independent copy, and synchronize source. Inspect hard links/COW and break sharing before writing so the patch cannot corrupt current and rollback copies together. Update client dependency references, resource length/ETag, and verify public bytes.

If another update changes the running version/configuration during deployment, stop this switch and reconcile differences rather than overwriting later work. Rollback scripts must also check current identity; an old rollback command is not universal. Without a production rollback rehearsal, report “rollback point retained/isolated validation,” not “production recovery verified.”

## 6. Production domains, certificates, and old entrypoints

Baota/Nginx manages sites, TLS, and reverse proxying. DNSPod or the current DNS provider manages resolution. Inspect them separately first.

- Check authoritative DNS for apex, www, and old subdomains, plus at least one independent public resolver. If needed, connect directly to the new IP with Host/SNI and compare whether an old site comes from the previous server or cache.
- For user-provided certificates, inspect SAN, validity, chain, public/private-key match, and public fingerprint. Keep keys only in restricted private paths. An apex/www certificate does not automatically cover other subdomains.
- Preserve paths and queries for HTTP→HTTPS, apex→canonical www, and old→production redirects. An old HTTPS entrypoint needs its own valid TLS before redirecting. A configured 308 with old-domain NXDOMAIN is still incomplete compatibility.
- Align canonical, Open Graph, JSON-LD, robots, sitemap, llms, and necessary environment values. Preserve existing product URLs where possible; define explicit redirects when changes are necessary.
- Snapshot records before DNS edits, change only current targets, and verify that email/other business records remain unaffected. After switching, collect authoritative/public resolution, ordinary public requests, and browser results. Distinguish transient propagation caches from final evidence.

## 7. Analytics, consultation, SEO/GEO, and maintenance

Load analytics once per document on public pages, excluding admin/API. Verify the correct ID, script, and beacon response. Verify report ingestion separately in its backend.

When consultation UI integrates with analytics, test actual click targeting. Apply mobile-hide rules only at confirmed breakpoints and retest desktop access and the site's own contact methods. A visible greeting does not establish configured per-message, offline, queue, or timeout auto-replies. Without a user request, do not send customer-service test messages or enable paid bots.

For SEO/GEO, first check server-visible body text, title, description, H1, structured data, robots, sitemap, llms/brand-fact pages, and reciprocal internal links. Then address procurement questions, brochure materials, real cases, and external evidence. FAQ body and JSON-LD share a source. Remove outdated translations from the sitemap while updates are pending rather than presenting old content as current facts.

Record submission, crawling, indexing, ranking, and AI citation separately. Submission receipts only prove receipt; verify crawler identity and HTTP. One brand-query appearance does not generalize to all keywords. For AI tests, record platform, time, question, source URL, and account-history interference. CAPTCHA encounters remain pending user presence and do not count as valid samples.

After release, inspect service health, critical paths, static assets, admin 401, unknown-route 404, forms/consultation, and videos on both layouts. Perform real writes only within authorization, avoiding leads customers could mistake for genuine inquiries. Record current faults and follow-up checks. An existing backup does not establish configured automatic offsite backups, renewals, or alerting.
