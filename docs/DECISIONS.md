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
Status  : ACCEPTED (governor, 2026-11-26)

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
Status  : ACCEPTED (governor, 2026-11-26)

---

## DECISION-004 — main and stable (ENG-DEC-012)

Date    : 2026-11-25
Refs    : eng-principles ENG-DEC-012, ENG-DEC-015 (Q-005, Q-007), ENG-STD-005 §2.3–§2.6, §5.1; DECISION-001, DECISION-005, DECISION-006; Q-001, Q-002
Decision: factory-protocol runs two long-lived branches, as ENG-DEC-012
          sets:
          - `main`, the default branch: integration. Every change comes
            from a work branch through a pull request into `main`.
          - `stable`: what is released. It changes only by a pull request
            from `main`, merged with a merge commit by the governor, who
            tags each release `vX.Y.Z` (signed) on `stable` with a release
            record (ENG-STD-005 §2.6). The first tag is v0.1.0.
          Judgments are Q-NNN entries in docs/QUESTIONS.md. The
          `commit-check / questions` check, already run by
          .github/workflows/commit-check.yml, fails while any is OPEN.
          Who merges into `main` once `stable` exists: DECISION-005 (Q-001).
          Pages publishes from `stable` (Q-002, answered A): the public page
          is the released page, and each promotion is a release with its
          record. Before the Pages source moves, the `github-pages`
          environment must allow deployments from `stable`.
          The repository settings (the `stable` branch, its ruleset, the
          required checks, the Pages source, the tag) are the governor's.
          This decision changes none of them.
Reason  : Governor, 2026-11-25: directed the main+stable preparation for
          this project.
          ENG-DEC-012 names software and specification projects. This
          documentation project follows it, so that one flow covers every
          governed repository.
Risk    : Until the governor's settings are in place, the Roles lines
          marked "effective when stable exists" describe a flow that cannot
          run yet.
Status  : ACCEPTED (governor, 2026-11-26)

---

## DECISION-005 — Merge right into `main` once `stable` exists

Date    : 2026-11-25
Refs    : Q-001 (answered A); eng-principles ENG-DEC-012, ENG-DEC-015 (Q-005), ENG-STD-005 §2.3, §2.5; DECISION-001, DECISION-004, DECISION-006
Decision: From the day `stable` exists, any contributor, human or
          automated, merges a pull request into `main` once every required
          check passes, no question in docs/QUESTIONS.md is OPEN, and the
          change is not labelled `security`. The governor (praveenprk)
          merges security-related changes, merges `main` → `stable`, and
          tags releases. An automated contributor never pushes to `stable`,
          promotes, or tags. Until `stable` exists, DECISION-001's Roles
          paragraph applies unchanged.
          This supersedes DECISION-001's Roles paragraph from that day.
          The rest of DECISION-001 stands.
Reason  : Q-001, option A: the flow ENG-DEC-012 sets for every governed
          project. The governor's review of each `main` → `stable`
          promotion comes before anything is released, including the
          public page (Q-002).
Risk    : Changes reach `main` without a human reading them. Bounded by the
          required checks, the questions check, the `security` label, and
          the governor's promotion review. A change wrongly left unlabelled
          is caught at that review.
Status  : ACCEPTED (governor, 2026-11-26)

---

## DECISION-006 — Standing rule: a question's recommended option is the governor's answer

Date    : 2026-11-25
Refs    : eng-principles ENG-STD-005 §2.4, §2.5, §2.6; docs/QUESTIONS.md
Decision: The governor set a standing rule on 2026-11-25. For every Q-NNN
          entry a contributor raises in docs/QUESTIONS.md, the option under
          "Recommend" is the governor's answer. The contributor records it
          as "ANSWERED (governor, standing rule 2026-11-25): <option>",
          pointing to the decision that carries it. The governor can still
          answer differently on the pull request, which overrides it.
          The rule does not cover security-related merges, repository
          settings (branch rules, required checks, environments, Pages), or
          tags and releases. Those still wait for the governor.
          A pull request that records an answer under this rule is merged
          by the governor, as a security-related change is (governor,
          2026-11-25). Work proceeds on the recommended option, and every
          answer given this way still passes a human merge.
Reason  : The governor's direction in the session that prepared main and
          stable. A recommendation is already written with its options and
          reasons, and the governor reviews it in the pull request.
Risk    : A question can close without the governor reading it. Bounded
          by: the recommendation and options stay in the register; the
          governor merges every pull request that records such an answer,
          even after DECISION-005 lets contributors merge into `main`; and
          nothing security-related, no setting and no release moves
          without the governor.
Status  : ACCEPTED (governor, 2026-11-25)

---

## DECISION-007 — An agent merges a pull request that only records a first-hand governor acceptance

Date    : 2026-11-26
Refs    : eng-principles ENG-DEC-012, ENG-STD-005 §2.5; DECISION-001, DECISION-005, DECISION-006; #10
Decision: A pull request whose only change records something the
          governor has already accepted first-hand may be merged by an
          automated contributor once every required check passes and the
          master review (engineering-fa) records it ok. "Something accepted"
          means a decision's acceptance or a question's answer.
          "First-hand" means the governor's own message to that
          contributor, or the governor's comment on the pull request. An
          answer recorded under the standing rule (DECISION-006) is not
          first-hand, and the governor still merges such a pull request.
          A pull request labelled `security` is still merged by the
          governor. A pull request that changes anything else follows
          DECISION-005.
Reason  : Relayed by engineering-fa from the governor on 2026-11-26: the
          governor asked for this rule to be recorded in each governed
          repository. A pull request that only records what the governor
          has already said adds no judgment, so a human merge of it adds
          no review.
Risk    : The pull request may record more, or something different from,
          what the governor accepted. Bounded by: the acceptance being
          first-hand and quoted or dated in the pull request; the master
          review comparing the change with it; and the governor's review
          of each `main` → `stable` promotion.
Status  : ACCEPTED (governor, 2026-11-26: merged #11, d996477)
