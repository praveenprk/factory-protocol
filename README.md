# factory-protocol

A visual explainer of the **ContextOS Factory Protocol**, the gated
production line ContextOS uses to build itself.

Open `index.html` in a browser.

## What it covers

- **The line:** ten stations, forward only:
  `INTAKE → RFC → SPEC → DESIGN → TEST → CODE → CI-CHECK → REFACTOR → DOC-REVIEW → DOC-UPDATE → CLOSED`
- **The line controller:** `factory/supervisor.sh`, a shell-only gate enforcer
  (routing sheet, release check, sha256 artifact integrity)
- **Floor rules:** serialization, context isolation (DECISION-019), artifact
  compression, adversarial critic, anchored commits
- **Batch record:** the manufacturing Electronic Batch Record and
  review-by-exception mapping from RFC-032
- **Release:** the governor's role before and after DECISION-039

Sources: ContextOS `AGENTS.md`, `docs/DECISIONS.md` (DECISION-017, -019, -039),
`factory/protocol/state-machine`, `factory/supervisor.sh`, RFC-032 §7.
