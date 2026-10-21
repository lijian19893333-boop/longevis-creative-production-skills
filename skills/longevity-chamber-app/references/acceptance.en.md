# Acceptance for affected paths

Record preconditions, action, expected and observed outcomes, version, evidence and gaps. These are scenarios to execute, not passing results.

1. Minimum/maximum/invalid parameters, saved readback, device refusal and timeout; observe drafts, configuration, targets and measurements separately.
2. Configuration and active sessions after re-entry, language change and app restart; do not replay old state unconditionally.
3. Authoritative state before/during disconnection and after reconnection; demo indicators, stale feedback, duplicate ACKs and late responses.
4. Normal, manual and fault termination with distinct cleanup. Mark unsupported pause or door control not applicable.
5. Alarm occurrence, recovery, latching and acknowledgement; distinguish informational warnings from blocking faults.
6. Wake, modal, disabled, submitting, empty and connection-failed states; verify touch behavior on the actual screen.
7. Maintenance roles, output requests versus physical feedback, exit/timeout recovery; execute only in an authorized test environment.
8. Clearing and upgrades have scoped, cancel, failure and recovery paths. UI checks do not establish actual data deletion or upgrades.

Distinguish not-run, simulation, UI, communication, bench, whole-machine and user acceptance. A single completion checkbox cannot represent all levels.
