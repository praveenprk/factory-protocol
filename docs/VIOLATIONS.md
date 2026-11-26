# VIOLATIONS.md
# factory-protocol — Violations Register
# Append only. No violation is ever removed. A violation may be marked
# RESOLVED with date and commit reference. Dates of merges are UTC. (eng-principles ENG-STD-006,
# templates/violation.md)
#
# Severity follows eng-principles ENG-STD-006 §2.3 (ENG-DEC-013); each
# entry names the rule (a–e) and its source. Severities are proposed by the
# contributor and confirmed by the governor.
#
# IDs: V-ENG-<standard>-<NN> = violation of an eng-principles standard.
#
# Evidence is read at main 1340fa7 (2026-11-15) and in the eng-principles
# audit report generated 2026-11-22T23:29Z (issue #3).

## Summary (2026-11-25)

| ID | Standard | Audit check | Severity | Status |
|----|----------|-------------|----------|--------|
| V-ENG-008-01 | ENG-STD-008 `contributing` | contributing | HIGH | RESOLVED |
| V-ENG-008-02 | ENG-STD-008 `security` | security | HIGH | RESOLVED |
| V-ENG-008-03 | ENG-STD-008 `tests` | tests | HIGH | OPEN (tests/ in CI; awaits DECISION-002) |
| V-ENG-004-01 | ENG-STD-004 §6.1 | fmt_lint | HIGH | RESOLVED |
| V-ENG-008-04 | ENG-STD-008 `required` | required | HIGH | RESOLVED |
| V-ENG-008-05 | ENG-STD-008 `dependabot` | dependabot | HIGH | RESOLVED |
| V-ENG-008-06 | ENG-STD-008 `ci` | ci | LOW | RESOLVED |
| V-ENG-006-01 | ENG-STD-006 §1 | registers | MEDIUM | RESOLVED |
| V-ENG-005-01 | ENG-STD-005 §6.1 | agents | MEDIUM | RESOLVED |
| V-ENG-005-02 | ENG-STD-005 §1.3, §1.5 | commit_check | MEDIUM | RESOLVED |

---

### V-ENG-008-01
SPEC says : ENG-STD-008 §2.2, check `contributing` (MUST): the repository has a CONTRIBUTING file.
Code does : No CONTRIBUTING.md at 1340fa7 (`git ls-files` lists LICENSE, NOTICE, README.md, factory-protocol.html, index.html). Audit: "no CONTRIBUTING.md".
Severity  : HIGH — rule b, OpenSSF Best Practices MUST `contribution`.
Impact    : A contributor cannot find how to propose a change or what is checked.
Fix       : CONTRIBUTING.md, with AGENTS.md for the full rules.
When      : This change.
Status    : RESOLVED — 2026-11-24, ae200f2 (#4).
Anchor    : #3

### V-ENG-008-02
SPEC says : ENG-STD-008 §2.2, check `security` (MUST): SECURITY.md with a private way to report a vulnerability.
Code does : No SECURITY.md at 1340fa7. GitHub private vulnerability reporting is enabled (`gh api repos/praveenprk/factory-protocol/private-vulnerability-reporting` → enabled: true, 2026-11-25), but nothing in the repository says so. Audit: "no SECURITY.md: no private way to report a vulnerability".
Severity  : HIGH — rule a gives MEDIUM (OpenSSF Scorecard Security-Policy); rule d raises it: security-related, never below HIGH.
Impact    : A reporter may disclose a problem in a public issue, for example a script injection in the page served on GitHub Pages.
Fix       : SECURITY.md pointing to private vulnerability reporting. Security-related (ENG-STD-005 §2.5): its own pull request, label `security`, merged by a human.
When      : Next change.
Status    : RESOLVED — 2026-11-24, 3e8e7c2 (#5).
Anchor    : #3

### V-ENG-008-03
SPEC says : ENG-STD-008 §2.2, check `tests` (MUST): automated tests.
Code does : No tests at 1340fa7. Nothing checks that index.html is factory-protocol.html in its document wrapper (README.md says it is), or that the page's stations and transitions match contextos factory/protocol/state-machine.
Severity  : HIGH — rule b, OpenSSF Best Practices MUST `test` (proposed; the governor confirms that it applies to a documentation-only project, which ENG-DEC-008 left `not assessed`. DECISION-002's TEST gate is the equivalent process ENG-DEC-015 Q-002 allows).
Impact    : The page can drift from the factory it describes, or from its own source file, without anyone noticing.
Fix       : tests/ run in CI: the wrapper check, and the page's transitions against a pinned copy of the contextos state machine (DECISION-002, TEST gate).
When      : CI change. Resolved when DECISION-002 is ACCEPTED and the first tests/ check runs in CI.
Status    : OPEN
Anchor    : #3

### V-ENG-004-01
SPEC says : ENG-STD-004 §6.1 — "Each project MUST pin one formatter and one linter per language and run them in CI." §0.1 (ENG-DEC-015): inline `<script>` is code.
Code does : factory-protocol.html and index.html each carry one inline `<script>` (`grep -c '<script' index.html factory-protocol.html` → 1, 1). No formatter or linter, and no CI (no .github/ in `git ls-files` at 1340fa7). Which languages §6.1 binds is not recorded (§0.2).
Severity  : HIGH — rule b, OpenSSF Best Practices MUST `warnings`.
Impact    : Script errors in the page are found only by someone opening it in a browser.
Fix       : DECISION-003 names the languages bound (§0.2): JavaScript in the inline script (Prettier 3.10.1, ESLint 10.15.0 with eslint-plugin-html 8.2.1) and Python in tests/ and scripts/ (ruff 0.17.6, check and format). The `lint` job of .github/workflows/ci.yml runs them; versions are pinned in package-lock.json and requirements-dev.txt.
When      : CI change.
Status    : RESOLVED — 2026-11-24, fba350e (#6).
Anchor    : #3

### V-ENG-008-04
SPEC says : ENG-STD-008 §2.2, check `required` (MUST): a build or test check is required to merge.
Code does : Ruleset `factory-protocol-ruleset` requires only "GitGuardian Security Checks" (`gh api repos/praveenprk/factory-protocol/rulesets/27276808`, 2026-11-25). There is no build or test check to require yet.
Severity  : HIGH — rule a, OpenSSF Scorecard Branch-Protection (High).
Impact    : A change that breaks the page can merge.
Fix       : After the CI change merges, the governor adds its jobs (`lint`, `test`, `links`, and `commit-check / check`) to the ruleset's required checks. Changing required checks is security-related (ENG-STD-005 §2.5) and is the governor's.
When      : After the CI change.
Status    : RESOLVED — 2026-11-27, GitHub API evidence read by the reviewer: active ruleset `factory-protocol-ruleset` (id 27276808, default branch) and active ruleset `stable-integrity` (id 28107503, `refs/heads/stable`) each require `GitGuardian Security Checks`, `lint`, `test`, `links`, `commit-check / check`, and `commit-check / questions`.
Anchor    : #3

### V-ENG-008-05
SPEC says : ENG-STD-008 §2.2, check `dependabot` (SHOULD): automated dependency updates.
Code does : No .github/dependabot.yml or Renovate configuration at 1340fa7.
Severity  : HIGH — rule a, OpenSSF Scorecard Dependency-Update-Tool (High).
Impact    : Once CI uses pinned actions and tools, they go stale silently.
Fix       : .github/dependabot.yml: weekly updates for GitHub Actions, npm (package.json) and pip (requirements-dev.txt), labelled `security` (DECISION-002).
When      : CI change.
Status    : RESOLVED — 2026-11-24, fba350e (#6).
Anchor    : #3

### V-ENG-008-06
SPEC says : ENG-STD-008 §2.2, check `ci` (MUST): CI runs on every pull request.
Code does : No workflow at 1340fa7. Audit: "no workflow runs on pull requests".
Severity  : LOW — rule a, OpenSSF Scorecard CI-Tests (Low).
Impact    : Nothing is checked before a merge except GitGuardian.
Fix       : .github/workflows/ci.yml runs on every pull request and on pushes to main: jobs `lint`, `test`, `links`.
When      : CI change.
Status    : RESOLVED — 2026-11-24, fba350e (#6).
Anchor    : #3

### V-ENG-006-01
SPEC says : ENG-STD-006 §1 — "Every project MUST keep three registers": decisions, violations, ICS.
Code does : None of the three at 1340fa7. Audit: "missing: ICS, decisions, violations".
Severity  : MEDIUM — rule c, eng-principles' own rule; it changes no behaviour of the page.
Impact    : Gaps and decisions are tracked only in eng-principles, not where a contributor to this project looks.
Fix       : docs/DECISIONS.md, this file, docs/conformance/factory-protocol-ICS.md (DECISION-001).
When      : This change.
Status    : RESOLVED — 2026-11-24, ae200f2 (#4).
Anchor    : DECISION-001

### V-ENG-005-01
SPEC says : ENG-STD-005 §6.1 — "Instructions for automated contributors MUST live in one tool-agnostic file at the repository root: AGENTS.md."
Code does : No AGENTS.md at 1340fa7. Audit: `agents` missing.
Severity  : MEDIUM — rule c, eng-principles' own rule; it changes no behaviour of the page.
Impact    : An automated contributor has no stated rules for this repository.
Fix       : AGENTS.md; CLAUDE.md only points to it.
When      : This change.
Status    : RESOLVED — 2026-11-24, ae200f2 (#4).
Anchor    : DECISION-001

### V-ENG-005-02
SPEC says : ENG-STD-005 §1.3 — "Every commit MUST carry at least one anchor that resolves to a governed entry". §1.5 — checked on the git host for everything a change brings to the default branch.
Code does : 0 of the 4 non-merge commits up to 1340fa7 carries an anchor (`git log --no-merges --format=%s 1340fa7`, e.g. 13ad193 "chore: license under Apache-2.0 with NOTICE"). No workflow calls eng-principles' shared commit check, and the ruleset does not require it. Audit: `commit_check` missing.
Severity  : MEDIUM — rule c, eng-principles' own rule; it changes no behaviour of the page.
Impact    : The reason for each change cannot be traced by machine.
Fix       : A workflow calling eng-principles' shared commit check pinned to a commit (ENG-DEC-009), with scripts/hooks/types and scripts/hooks/anchors (this change); then the governor requires `commit-check / check`. History is not rewritten: resolved forward only.
When      : CI change, then the governor's ruleset change.
Status    : RESOLVED — 2026-11-27, GitHub API evidence read by the reviewer: active ruleset `factory-protocol-ruleset` (id 27276808, default branch) and active ruleset `stable-integrity` (id 28107503, `refs/heads/stable`) each require `GitGuardian Security Checks`, `lint`, `test`, `links`, `commit-check / check`, and `commit-check / questions`.
            History: PARTIALLY_RESOLVED — 2026-11-24, fba350e (#6): .github/workflows/commit-check.yml calls the shared check pinned to eng-principles 8613443. Not yet required by the ruleset (V-ENG-008-04).
Anchor    : DECISION-001
