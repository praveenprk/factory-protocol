# Contributing to factory-protocol

Thank you for looking. This repository holds one page: a visual explainer of
the ContextOS Factory Protocol. The full rules for every contributor, human
or automated, are in [AGENTS.md](AGENTS.md). This page is the short version.

## Before you start

- **Is it already known?** Check the
  [issues](https://github.com/praveenprk/factory-protocol/issues),
  [docs/DECISIONS.md](docs/DECISIONS.md) and
  [docs/VIOLATIONS.md](docs/VIOLATIONS.md).
- **The page follows the factory, not the other way round.** If the page says
  something the factory does not do, the fix is to the page, with the
  contextos source that shows it (docs/DECISIONS.md DECISION-002).
- **Found a security problem?** Do not open a public issue. Report it
  privately through the repository's Security tab ("Report a
  vulnerability"). See [SECURITY.md](SECURITY.md).

## Viewing the page

Open `index.html` in a browser, or see
https://praveenprk.github.io/factory-protocol/. `factory-protocol.html` is
the same page without the `<html>`, `<head>` and `<body>` wrapper. Edit
`factory-protocol.html`; `index.html` is built from it and the two must not
drift.

## How a change gets in

1. **Open an issue** saying what is wrong or missing, and for a change to
   what the page says about the factory, which contextos file says otherwise
   (at a commit). Typos, formatting and broken links need no issue beyond
   the anchor (DECISION-002, trivial class).
2. **Branch** from `main`: `type/ANCHOR-description`, e.g.
   `fix/12-ci-check-station-label`. Never commit to `main`.
3. **Title and every commit:** `type(scope): description — ANCHOR`.
   - Types: feat, fix, test, refactor, docs, chore, design.
   - An anchor is something that exists: `#12` (an issue or pull request
     here), `DECISION-002`, `V-ENG-008-03`, or an eng-principles entry such
     as `ENG-STD-005`.
4. **No co-author or tool-attribution lines** in commits or the
   description.
5. **Fixing a recorded violation?** Update docs/VIOLATIONS.md in the same
   pull request.
6. **Merging:** the governor merges into `main` (AGENTS.md: Roles).

## Conduct

Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Licence

By contributing you agree that your contribution is licensed under the
[Apache License, Version 2.0](LICENSE). The licence does not grant rights to
the "Factory Protocol" name ([NOTICE](NOTICE)).
