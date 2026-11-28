# factory-protocol — Implementation Conformance Statement (ICS)

This file records factory-protocol's conformance against the eng-principles
standards (ENG-STD-006). Vocabulary: `conformant` / `partial` / `not yet` /
`n/a` / `not assessed`. Nothing is `conformant` without evidence. A `not
assessed` row states why, and what assessing it needs (ENG-DEC-015).

Date of last update: 2026-11-25
Baseline: main fba350e (#4, #5, #6 merged). eng-principles audit (audit/audit.py at 86d9e76, kinds `docs`) run 2026-11-24T21:12Z against fba350e: MUST 12 of 14, SHOULD 5 of 6.

## What this project is

A documentation-only project: one page describing the ContextOS Factory
Protocol (index.html, DECISION-008). It has no specification of its own;
what it describes is defined in contextos (DECISION-002).

## Maturity (ENG-STD-009)

| Level | Read | Evidence | Blocks the next level |
|-------|------|----------|-----------------------|
| L2 | 2026-11-23 (eng-principles CONFORMANCE.md) | A document takes the level of what it describes. The contextos factory is at L2: its supervisor has no tests, and one run is committed | L3: the factory reaches L3, and the page is checked against the state machine that actually runs (contextos factory/protocol/state-machine) |

## eng-principles standards

| Standard | Status | Evidence | Open violations |
|----------|--------|----------|-----------------|
| ENG-STD-001 Language & IDs | not assessed | Not yet read against this repository. Needs a read of the page and registers against §1 and §2 | — |
| ENG-STD-002 Lifecycle gates | partial | DECISION-002 maps the gates and records the trivial class (§5.4). It is PROPOSED until the governor decides the trivial class (§3.2). tests/test_page.py checks the page's stations and gates against its own line and README.md; a check against contextos factory/protocol/state-machine is not in place (contextos is private) | V-ENG-008-03 |
| ENG-STD-004 Construction | partial | §0.2, §6.1: DECISION-003 records the languages bound (JavaScript in the inline script, Python in tests/ and scripts/); Prettier, ESLint and ruff, pinned, run in the `lint` job of .github/workflows/ci.yml (V-ENG-004-01, resolved). Other clauses not assessed: needs a review of the inline script against §1–§4 | — |
| ENG-STD-005 Change control | partial | Ruleset `factory-protocol-ruleset`: pull request required, no deletion, no force-push, merge commits only (`gh api repos/praveenprk/factory-protocol/rulesets/27276808`). AGENTS.md (V-ENG-005-01, resolved). The shared commit check is called by .github/workflows/commit-check.yml, pinned to eng-principles 8613443, but not yet required by the ruleset. Commits before adoption are unanchored | V-ENG-005-02 |
| ENG-STD-003 Design | n/a | The inline script is construction, held to ENG-STD-004. It has no design surface: no interfaces, modules or contracts, and no substrate beyond the browser | — |
| ENG-STD-006 Registers | partial | docs/DECISIONS.md, docs/VIOLATIONS.md, this file (V-ENG-006-01, resolved). DECISION-001 is ACCEPTED (governor, 2026-11-26); conformant once that acceptance is merged and its merge commit is cited here | — |
| ENG-STD-007 Quality model | not assessed | No quality characteristics are constrained, as there is no SPEC here. Needs DECISION-002 accepted, then a read of which ENG-STD-007 characteristics apply to a page | — |
| ENG-STD-008 Contributor readiness | partial | Audit at fba350e (2026-11-24T21:12Z): every check that applies to `docs` passes except three, all repository settings: `required` (no build or test check required to merge, V-ENG-008-04), `commit_check` (the shared check is called but not required, V-ENG-005-02), `about` (no topics). Checks for rust, python and spec kinds report n/a for a documentation project (changelog, semver, releases, signed, supply, cargo_meta, msrv, docs, pyproject, py_min, bcp14, seccons, trace) | V-ENG-008-04, V-ENG-005-02 |
| ENG-STD-009 Evidence and maturity | conformant | Maturity row above, as read by eng-principles CONFORMANCE.md (2026-11-23) | — |
