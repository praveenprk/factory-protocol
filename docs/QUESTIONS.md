# QUESTIONS.md — factory-protocol

Open questions for the governor, one entry per question, in the format of
eng-principles templates/question.md (ENG-STD-005 §2.4, ENG-DEC-012). The
pull request that raises a question adds its entry here, and the governor
answers on that pull request. The `commit-check / questions` check fails
while any entry is OPEN, so nothing reaches `main` with an open question. An
answer that changes how this project works becomes a DECISION-NNN entry in
docs/DECISIONS.md. Entries are never deleted (ENG-STD-006 §2.1).

Standing rule (DECISION-006): the Recommend option is the governor's answer.
It is recorded as "ANSWERED (governor, standing rule 2026-11-25): <option>".
The governor can override it on the pull request. A pull request that records
an answer this way is merged by the governor. Security merges, settings and
tags still wait for the governor.

---

### Q-001
Scenario : Under ENG-DEC-012, once `stable` exists, an automated
           contributor merges a pull request into `main` when every required
           check passes, no question is OPEN, and the change is not
           security-related. DECISION-001 says the opposite for this
           project: "This project grants no contributor, human or automated,
           the merge right ENG-DEC-012 gives (refined by ENG-DEC-015,
           Q-005), until the governor decides otherwise here." AGENTS.md
           and CONTRIBUTING.md now carry the ENG-DEC-012 rule, marked
           "effective when stable exists". Without an answer, the two
           conflict on the day `stable` is created.
Options  : A — Grant the merge right when `stable` exists: a new decision
               supersedes DECISION-001's Roles paragraph. An automated
               contributor merges into `main` when the required checks pass,
               no question is OPEN, and the change is not labelled
               `security`. The governor merges `main` → `stable` and tags.
           B — Keep DECISION-001 as it is: only the governor merges into
               `main`, even after `stable` exists. The Roles lines added by
               this pull request are withdrawn.
Recommend: A, because it is the flow ENG-DEC-012 sets for every project,
           and the governor's review of each `main` → `stable` promotion
           still comes before anything is released.
Raised by: the pull request that adds this file (chore/ENG-DEC-012-main-stable-prep)
Status   : ANSWERED (governor, standing rule 2026-11-25): A → DECISION-005

### Q-002
Scenario : GitHub Pages publishes the page from `main`
           (`gh api repos/praveenprk/factory-protocol/pages` → branch main,
           path /). Under ENG-DEC-012, `main` is integration and `stable`
           is what is released. If Pages stays on `main`, a change merged
           into `main` by an automated contributor (Q-001 A) is public
           within minutes, before the governor's promotion review.
Options  : A — Publish from `stable`: the public page is the released page,
               and each promotion is a release with its record (ENG-STD-005
               §2.6). Changes: the Pages source setting.
           B — Keep publishing from `main`: the page tracks integration, and
               `stable` and tags only mark reviewed points.
Recommend: A, because the published page is what readers rely on. It
           should pass the same human review as a release.
Raised by: the pull request that adds this file (chore/ENG-DEC-012-main-stable-prep)
Status   : ANSWERED (governor, standing rule 2026-11-25): A → DECISION-004
