# factory-protocol

A visual explainer of the **ContextOS Factory Protocol**, the gated
production line ContextOS uses to build itself.

> **Work in progress.** The Factory Protocol is still being strengthened.
> Content here may change as the protocol evolves.

View it live at https://praveenprk.github.io/factory-protocol/ or open
`index.html` in a browser. `factory-protocol.html` is the same page
without the document wrapper (the source used to build `index.html`).

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). The page
follows the factory it describes: a correction cites the contextos source
that shows it. Decisions, known gaps and conformance are recorded in
[docs/DECISIONS.md](docs/DECISIONS.md), [docs/VIOLATIONS.md](docs/VIOLATIONS.md)
and [docs/conformance/factory-protocol-ICS.md](docs/conformance/factory-protocol-ICS.md).

## License

Licensed under the [Apache License, Version 2.0](LICENSE). See [NOTICE](NOTICE)
for copyright and trademark information. The license does not grant rights to
the "Factory Protocol" name.
