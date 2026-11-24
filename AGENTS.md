# AGENTS.md — factory-protocol

Instructions for every contributor, human or automated, whatever the model
or tool. Tool-specific files (CLAUDE.md and the like) only point here and
carry no rules (eng-principles ENG-STD-005 §6). Rules that bind agents also
bind humans.

factory-protocol follows eng-principles (docs/DECISIONS.md DECISION-001).
It is a documentation-only project: one page describing the ContextOS
Factory Protocol. What the page describes is defined in contextos, not here
(DECISION-002).

## Roles

- The governor (praveenprk) is the only one who merges into `main`. The
  governor accepts decisions and confirms violation severities.
- Contributors propose decisions (Status PROPOSED), file violations with
  evidence, and open pull requests. They do not merge into `main`, push to
  it, or decide.
- Releases: none. The page is published from `main` by GitHub Pages. There
  is no `stable` branch: the main+stable migration (ENG-DEC-012) is deferred
  by the governor. Do not start it.

## Before work

- Read docs/DECISIONS.md and docs/VIOLATIONS.md. The change, decision or
  gap may already be recorded. Open work is in the GitHub issues.
- For a change to what the page says the factory does, find the contextos
  source that says it (factory/protocol/state-machine, factory/supervisor.sh,
  AGENTS.md, docs/DECISIONS.md, an RFC) and cite it at a commit
  (DECISION-002).

## Order of work (DECISION-002)

1. An issue states what the page gets wrong or lacks, and the contextos
   source that says otherwise.
2. A check in tests/ that fails first, where the fact can be checked by
   machine; otherwise the pull request names the source line.
3. Then the page: edit factory-protocol.html, and regenerate index.html from
   it with `python3 scripts/build_index.py` (index.html is the same page
   inside a document wrapper; tests/ fails if it is stale).
4. Then README.md and the registers.

Trivial changes (DECISION-002: typos, formatting, link fixes, dependency
updates, contributor documents) skip steps 1 and 2 and still carry an anchor.
Dependency and GitHub Action updates are supply-chain changes: they carry
the label `security` and only the governor merges them.

## Changes

- Every change traces to an anchor that resolves: DECISION-NNN or
  V-ENG-NNN-NN in this repository, ENG-* in eng-principles, or #N (an issue
  or pull request of this repository). No anchor, no work.
- Branch: `type/ANCHOR-short-description` (e.g. `docs/3-registers-and-contributor-docs`).
- Commit and pull request title: `type(scope): description — ANCHOR[, ANCHOR…]`.
  Types: feat fix test refactor docs chore design (scripts/hooks/types).
- No co-author, AI attribution, or "Generated with" lines in commits or pull
  request descriptions. A pull request description written by an automated
  contributor ends with `Session-Id: <session id>`.
- Never force-push or rewrite pushed history.
- A violation fix updates docs/VIOLATIONS.md in the same change.
- Do not mark anything `conformant` in docs/conformance/factory-protocol-ICS.md
  without cited evidence (a test, a commit, or a command and its output).
- A change touching SECURITY.md, workflow token permissions, secrets,
  branch rules, required checks, or a dependency or GitHub Action version
  is security-related (ENG-STD-005 §2.5):
  it carries the label `security` and only a human merges it.

## Enforcement

On GitHub, not on the contributor's machine (DECISION-001): the branch
ruleset requires a pull request and forbids deletion and force-pushes.
eng-principles' shared commit check reads scripts/hooks/types and
scripts/hooks/anchors once a workflow calls it (V-ENG-005-02).
