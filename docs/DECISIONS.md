# DECISIONS.md
# factory-protocol — Decisions Register
# Append only. A decision may be superseded. It is never removed.
# Format: ID — Title | Date | Refs | Decision | Reason | Risk | Status
# (eng-principles ENG-STD-006, templates/decision.md)

---

## DECISION-001 — Adopt eng-principles

Date    : 2026-11-25
Refs    : eng-principles ENG-DEC-008 (registers this project), ENG-STD-005, ENG-STD-006, ENG-STD-008, ENG-DEC-009, ENG-DEC-015; issue #3
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
          Roles (ENG-STD-005 §2.6): the governor (PK, GitHub praveenprk) is
          the only one who merges into `main`. This project grants no
          contributor, human or automated, the merge right ENG-DEC-015
          allows, until the governor decides otherwise here. There are no
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
          - dependency and GitHub Action updates with no change to the page;
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
