# factory-protocol — Implementation Conformance Statement (ICS)

This file records factory-protocol's conformance against the eng-principles
standards (ENG-STD-006). Vocabulary: `conformant` / `partial` / `not yet` /
`n/a` / `not assessed`. Nothing is `conformant` without evidence. A `not
assessed` row states why, and what assessing it needs (ENG-DEC-015).

Date of last update: 2026-11-25
Baseline: main 1340fa7, plus the change that adds this file (#3).

## What this project is

A documentation-only project: one page describing the ContextOS Factory
Protocol (factory-protocol.html, and index.html built from it). It has no
specification of its own; what it describes is defined in contextos
(DECISION-002).

## Maturity (ENG-STD-009)

| Level | Read | Evidence | Blocks the next level |
|-------|------|----------|-----------------------|
| L2 | 2026-11-23 (eng-principles CONFORMANCE.md) | A document takes the level of what it describes. The contextos factory is at L2: its supervisor has no tests, and one run is committed | L3: the factory reaches L3, and the page is checked against the state machine that actually runs (contextos factory/protocol/state-machine) |

## eng-principles standards

| Standard | Status | Evidence | Open violations |
|----------|--------|----------|-----------------|
| ENG-STD-001 Language & IDs | not assessed | Not yet read against this repository. Needs a read of the page and registers against §1 and §2 | — |
| ENG-STD-002 Lifecycle gates | partial | DECISION-002 maps the gates and records the trivial class (§5.4). It is PROPOSED until the governor decides the trivial class (§3.2). tests/test_page.py checks the page's stations and gates against its own line and README.md; a check against contextos factory/protocol/state-machine is not in place (contextos is private) | V-ENG-008-03 |
| ENG-STD-003 Design | n/a | No software design: one static page with one inline script | — |
| ENG-STD-004 Construction | partial | §0.2, §6.1: DECISION-003 records the languages bound (JavaScript in the inline script, Python in tests/ and scripts/); Prettier, ESLint and ruff, pinned, run in the `lint` job of .github/workflows/ci.yml (V-ENG-004-01, resolved). Other clauses not assessed: needs a review of the inline script against §1–§4 | — |
| ENG-STD-005 Change control | partial | Ruleset `factory-protocol-ruleset`: pull request required, no deletion, no force-push, merge commits only (`gh api repos/praveenprk/factory-protocol/rulesets/27276808`). AGENTS.md (V-ENG-005-01, resolved). The shared commit check is called by .github/workflows/commit-check.yml, pinned to eng-principles 8613443, but not yet required by the ruleset. Commits before adoption are unanchored | V-ENG-005-02 |
| ENG-STD-006 Registers | partial | docs/DECISIONS.md, docs/VIOLATIONS.md, this file (V-ENG-006-01, resolved). DECISION-001 is PROPOSED | — |
| ENG-STD-007 Quality model | not assessed | No quality characteristics are constrained, as there is no SPEC here. Needs DECISION-002 accepted, then a read of which ENG-STD-007 characteristics apply to a page | — |
| ENG-STD-008 Contributor readiness | not yet | Present: README, licence (Apache-2.0), CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md (private vulnerability reporting, V-ENG-008-02 resolved), AGENTS.md, issue and pull request templates, registers, branch rules. CI on every pull request (`lint`, `test`, `links`), tests/ (8 tests), linting, Dependabot. Missing: a required build check and the shared check required (both governor ruleset changes); DECISION-002 accepted for `tests`; repository topics (`about`, a governor setting) | V-ENG-008-03, V-ENG-008-04, V-ENG-005-02 |
| ENG-STD-009 Evidence and maturity | conformant | Maturity row above, as read by eng-principles CONFORMANCE.md (2026-11-23) | — |
