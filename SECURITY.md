# Security policy

## Supported versions

The latest release on `stable`, which GitHub Pages publishes
(https://praveenprk.github.io/factory-protocol/), is the only supported
version.

## Reporting a vulnerability

Please report privately. Do not open a public issue.

Use GitHub's private vulnerability reporting:
**[Report a vulnerability](https://github.com/praveenprk/factory-protocol/security/advisories/new)**
(the repository's Security tab → "Report a vulnerability").

If you cannot use GitHub, email the maintainer at
**justpraveenhere@protonmail.com**, with "factory-protocol security" in the
subject.

Include:

- what is affected: the page, its inline script, a workflow, or the
  published site;
- what an attacker can do, and the steps or input that show it;
- any fix you suggest.

You will get an acknowledgement within 7 days, in the advisory thread or by
email. Once a fix is
merged, the advisory is published with credit to you, unless you ask not to
be named.

## In scope

- **The page and its inline script** (index.html),
  for example script injection, or loading content from an origin the page
  does not name.
- **The workflows** in .github/workflows: a way to run code with the
  workflow token, or to get secrets.
- **The published GitHub Pages site**, where it differs from `stable`.

## Not a vulnerability

- The page describing the factory wrongly. That is a correction: open an
  issue with the "Correction" template.
- Vulnerabilities in the factory itself are outside this repository's
  scope. Report them through the same private channel above.
