# DECISIONS.md
# factory-protocol — Decisions Register
# Append only. A decision may be superseded. It is never removed.
# Format: ID — Title | Date | Refs | Decision | Reason | Risk | Status
# (eng-principles ENG-STD-006, templates/decision.md)

---

## DECISION-001 — Adopt eng-principles

Date    : 2026-11-25
Refs    : eng-principles ENG-DEC-008 (registers this project), ENG-STD-005, ENG-STD-006, ENG-STD-008, ENG-DEC-009, ENG-DEC-012, ENG-DEC-015 (Q-005); issue #3
Decision: factory-protocol follows eng-principles. Its registers are:
          | eng-principles           | factory-protocol                          |
          |--------------------------|-------------------------------------------|
          | Decisions                | this file (DECISION-NNN)                  |
          | ENG-standard violations  | docs/VIOLATIONS.md (V-ENG-NNN-NN)         |
          | ENG-standard conformance | docs/conformance/factory-protocol-ICS.md  |
          | Agent instructions       | AGENTS.md (CLAUDE.md only points to it)   |
          Anchors: DECISION-NNN and V-ENG-NNN-NN resolve in this
          repository; ENG-* in eng-principles; #N is an issue or pull
          request of this repository. scripts/hooks/types and
          scripts/hooks/anchors are the configuration eng-principles'
          shared commit check reads (ENG-DEC-009).
          Enforcement is on GitHub, not on the contributor's machine. No
          local hooks are vendored: a local hook never runs on a merge made
          on GitHub, and it can be skipped.
          Roles (ENG-STD-005 §2.6): the governor (praveenprk) is
          the only one who merges into `main`. This project grants no
          contributor, human or automated, the merge right ENG-DEC-012
          gives (refined by ENG-DEC-015, Q-005), until the governor decides otherwise here. There are no
          releases and no `stable` branch: the main+stable migration
          (ENG-DEC-012) is deferred by the governor.
Reason  : The project has none of the registers ENG-STD-006 requires, and
          the eng-principles audit (2026-11-22T23:29Z) lists the gaps
          (#3). fid and phasectl adopted the same way, so a contributor who
          knows one finds the same layout here.
Risk    : Commits made before adoption (6767f6e..13ad193) carry no anchors.
          History is not rewritten (V-ENG-005-02).
Status  : PROPOSED

---

## DECISION-002 — Change process for a documentation-only project, and its trivial class

Date    : 2026-11-25
Refs    : eng-principles ENG-STD-002 §3, §5.2, §5.4 (ENG-DEC-015); ENG-STD-009 (maturity); issue #3
Decision: factory-protocol describes the ContextOS Factory Protocol. What
          it describes is defined in contextos, not here. So the gates are
          met as follows (ENG-STD-002 §5.2):
          | Gate   | Artifact that meets the exit condition |
          |--------|----------------------------------------|
          | RFC    | An issue stating what the page gets wrong or lacks, and the contextos source that says otherwise |
          | SPEC   | That contextos source (factory/protocol/state-machine, factory/supervisor.sh, AGENTS.md, docs/DECISIONS.md, an RFC), cited at a commit |
          | TEST   | A check in tests/ that compares the page with the cited source, and fails before the page changes, where the fact can be checked by machine; otherwise a review note in the pull request naming the source line |
          | BUILD  | The change to factory-protocol.html, with index.html regenerated from it |
          | REFINE | README.md and the registers updated |
          Trivial class (§3.1, §3.2): may skip RFC, SPEC and TEST, and still
          carries an anchor:
          - typos, grammar and wording that changes no stated fact;
          - formatting, including formatter output;
          - fixing a broken link to the same target;
          - dependency and GitHub Action updates with no change to the page.
            These are supply-chain changes, so they are security-related
            (ENG-STD-005 §2.5, ENG-DEC-013): they carry the label `security`
            and only the governor merges them;
          - changes to contributor documents and registers that add no rule.
          Anything that changes what the page says the factory does
          (stations, gates, roles, rules, transitions) is not trivial.
Reason  : ENG-STD-002 §5.4 requires a documentation-only project to record
          its trivial class once (eng-principles CONFORMANCE.md, ENG-STD-002
          row for this project). Mapping the gates to the contextos sources
          keeps the page as accurate as the factory it describes, which is
          what moves it up maturity levels (ENG-STD-009; #3).
Risk    : Most facts on the page are prose. Until tests cover them, only
          review checks that they match contextos.
Status  : PROPOSED (the trivial class is the governor's to decide, ENG-STD-002 §3.2)

---

## DECISION-003 — Languages bound by ENG-STD-004 §6.1, and their tools

Date    : 2026-11-25
Refs    : eng-principles ENG-STD-004 §0, §6.1, §7 (ENG-DEC-015); V-ENG-004-01, V-ENG-008-03, V-ENG-008-05, V-ENG-008-06; issue #3
Decision: §6.1 binds two languages here (§0.2):
          | Language   | Where                                  | Formatter          | Linter |
          |------------|----------------------------------------|--------------------|--------|
          | JavaScript | inline `<script>` in factory-protocol.html | Prettier 3.10.1 (formats the whole page) | ESLint 10.15.0, @eslint/js recommended, eslint-plugin-html 8.2.1 |
          | Python     | tests/, scripts/                        | ruff 0.17.6 format | ruff 0.17.6 check (ruff.toml) |
          index.html is generated from factory-protocol.html by
          scripts/build_index.py and is not formatted or linted itself;
          tests/test_page.py fails if it is stale. Workflow `run:` steps are
          held to §4 and §7 by review only.
          Dependencies (§7.1): the four npm packages and ruff are
          development tools only; nothing is shipped to the page. Versions
          are exact (package-lock.json, requirements-dev.txt) and Dependabot
          proposes updates. Python tests use the standard library only.
Reason  : The audit's `fmt_lint` check detects the inline script as
          JavaScript, and the tests added for V-ENG-008-03 are Python.
          Prettier and ESLint are what the audit names for JavaScript, and
          ruff is what fid and eng-principles already use. Rejected: Biome
          (does not lint scripts inside HTML), and JavaScript tests: the
          tests read the page as text and need nothing beyond the Python
          standard library, so testing the page needs no Node runtime or
          test framework. As a consequence, the audit's `tests` check,
          which looks for Rust or Python tests, finds them.
Risk    : Dependabot's pull requests carry no anchor, so the shared commit
          check refuses them; the governor retitles them or recreates their
          commits. Reformatting the page with Prettier is a one-off
          whitespace change (DECISION-002, trivial class).
Status  : PROPOSED
