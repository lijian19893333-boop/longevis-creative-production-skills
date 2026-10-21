---
name: longevity-science-video
description: Use when producing science explainer videos or establishing a science-video workflow, including research verification, scripts, storyboards, mechanism animation, narration, subtitles, and video acceptance.
---

# Longevity · LONGEVIS Science Video Workflow

[简体中文](SKILL.zh-CN.md)

Take a topic through to a reviewable video, distinguishing scientific verification, technical file checks, and the user's aesthetic acceptance. This public package supplies a working method and example brief, not a video-rendering project, voice model, commercial assets, or paid-service accounts.

## 1. Discover the environment and define the task

Find the current project's documentation, source, dependencies, and entrypoints first; confirm that tools actually exist. Reuse an existing project and create a new film version where possible. Without an existing project, establish one with currently available tools rather than assuming particular commands or components exist.

Use the user's materials to establish topic, audience, duration, aspect ratio, language, and style. Proceed where these can be inferred; ask only for missing information that affects production. Use the requested narration and subtitle languages, or the conversation language when unspecified. Default to landscape 1080p. Report actual duration and specifications at delivery. Copy the [example brief](assets/brief.example.json) if useful; its data and narration fields are placeholders.

## 2. Scientific facts and storyboard

Consult authoritative sources and record title, link, access date, and the specific statement supported. Map each key narration statement to a source. Separate verified facts, unverified user statements, plans, and design examples. Do not infer a particular product's treatment effects from a basic mechanism. Product models and parameters require currently confirmed material.

Structure the script as “phenomenon or question → mechanism → boundaries and applications.” For each shot record visuals, narration, subtitles, duration, and sourceIds. Narrow unsupported scientific claims or mark them pending verification; do not invent sources.

## 3. Choose the production route

- Use frame-driven Remotion / Three.js animation for mechanisms, data, and processes when appropriate. Read the relevant skills available in the environment or current official documentation before use.
- Use native Blender geometry, materials, lighting, and cameras, or assets the user has rights to use, for people, products, and spaces.
- Mixed films share narration, subtitles, and a timeline. State the completion status of mechanism sketches and finished 3D footage separately.
- Default to local prototypes first. Use LibTV or another external generation service only when the user explicitly chooses it, checking cost and authorization scope.

Set visual direction from the current brief. Do not inherit people, structures, brands, or parameters from another project. Motion must express the mechanism itself, such as flow, exchange, deformation, or signal transmission; moving the camera alone does not demonstrate a moving mechanism.

## 4. Audio, subtitles, and versions

Test a representative passage and listen for terminology, transitions, and pacing before generating the full narration. Reusing an approved voice still requires acceptance of the new text. Clearly label system speech used as a placeholder; do not automatically treat it as professional narration. Voice cloning requires samples the user has rights to use.

Build the timeline from actual sentence-level audio durations. Subtitles and narration may use different languages but must preserve meaning. Regenerate derived timelines after script changes. Give each film and delivery an independent version rather than overwriting previous work.

## 5. Export, check, and deliver

Validate the project before export. Discover actual commands from project documentation; do not invent successful execution.

Check decoding, duration, resolution, audio tracks, and subtitles in the actual export. Sample frames from every shot and scene boundary. Compare several time points in mechanism sequences to confirm that the intended region actually moves. Use a real player to inspect playback and audio/video synchronization.

Deliver the actual MP4, editable source or storyboard, subtitles, and usage instructions. State checks actually performed and remaining dependencies. File generation, upload, actual playback, and user acceptance are different states. If the environment or a service is unavailable, preserve completed work and explain the missing conditions.
