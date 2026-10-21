---
name: longevity-chamber-app
description: "Use when specifying or reviewing equipment control screens, apps or HMIs, including settings, state machines, communication contracts and handoff acceptance; not for storefronts or brand websites."
---

[简体中文](SKILL.zh-CN.md)

# Longevity · LONGEVIS Equipment Control Apps

Connect interfaces, equipment capabilities, states and evidence. This public edition supplies specification methods and blank templates. It contains no product formulas, production parameters, private protocols, passwords, application source or implementation that drives equipment.

## Start from the current project

Identify the official product name, model capabilities, screen/orientation, source and firmware versions, and task scope: specification, UI, interaction, communication or platform migration. Preserve the existing technical route. Android, WebView and HMI/PLC implementations are not interchangeable merely because their screens look similar. Complete supported work and ask only for facts that materially affect subsequent decisions.

Keep requirement status, implementation status, verification status and source separate. Record confirmed requirements, visible code, builds, installation, simulation, communication, bench tests, whole-machine tests and user acceptance individually. An archive or screenshot cannot establish hardware verification.

## Specify features

Review startup/standby, home, modes/parameters, running, completion, alarms, records, media and maintenance according to actual capabilities. These are review categories, not mandatory modules for every device. Provide pause, door locks, adjustable flow, position feedback or OTA only when supported by the current equipment evidence.

For each feature define entry/role, allowed states, input/unit/range/step/default source, action, acknowledgement and feedback, failure recovery, persistence, evidence and acceptance. Use the [feature template](templates/function-spec.en.md) and [blank register](templates/feature-register.csv). Mark unknown ranges as pending specification. Continue review in explicitly labeled simulation instead of guessing production values from old screenshots.

## Parameters and settings

Classify settings by who can change them, in which state, where they persist and when they apply. Record `key, label, unit, type, default_source, range, step, editable_states, role, storage, apply_when, readback, rollback, source`.

Separate edit drafts, saved configuration, transmitted targets and device measurements. A successful save does not prove hardware application. Display units may convert; communication units follow the contract. Navigation or language changes should not accidentally reset active sessions. Check migration, missing/out-of-range values, duplicate submission, mismatched readback, re-entry and restart persistence. Preserve current authentication and maintenance roles; do not copy another device's password or password-free behavior.

## State and communication

Separate UI, product rules, device adaptation and controller responsibilities. Represent connection, session, command and alarm states independently. Define the authoritative timer, parameter application point, post-stop cleanup, reconnection and restart behavior. A button press, received packet, business ACK, asserted output and completed mechanism movement are different states. Without real feedback, do not show “position reached.”

Record physical interface, rate, address, frame/checksum, scale factors, commands/status, timeout, idempotency, versions and logs. Read authoritative state on reconnection before blindly replaying non-idempotent commands such as start; the precise policy belongs to the current product specification.

Define disconnected startup, numerical warnings, hard faults, communication loss, app restart, controller restart/power loss and supported mechanical feedback changes individually. Specify affected outputs, timer behavior, recovery conditions and messages. App disconnection and controller power loss are different events. Make demo/Mock status visible; never mask a real disconnection with automatic demonstration. Writing documentation does not authorize physical operation.

## UI, data and acceptance

Preserve approved styling and layout. Keep values, buttons, tables and essential states editable. At the actual screen dimensions inspect normal, selected, disabled, submitting, failed, empty, disconnected, modal and wake behavior. A wake touch must not pass through to a run control.

Logs associate version, session, action, parameters, result, time and termination reason. For clearing data define exact scope, retained data, active-state restrictions, confirmation, transactions and recovery. Implement upgrades against actual compatibility, source/signature verification and failure handling; a button does not establish OTA capability.

Use the [acceptance scenarios](references/acceptance.en.md) for affected paths. Deliver the necessary feature register, parameter dictionary, state/exception tables, interface mapping, preview or installer, and observed test records. A complete specification may include explicit not-applicable entries. Report build success and whole-machine acceptance separately.

## Example

“Use this skill to review settings persistence and reconnection in an existing control screen. Preserve the framework; document four parameter-value stages, timer authority, ACK versus physical feedback, and verifiable acceptance cases. Do not connect equipment.”
