---
name: pull-request-message
description: Draft clear pull request or merge request descriptions from repository changes, using an opinionated template with motivation, modifications, result, and validation. Also improve existing PR/MR description drafts when asked.
compatibility: Requires Git when deriving descriptions from local repository changes.
---

# Pull Request Message

Use this skill when the user asks to draft, improve, rewrite, or review a pull
request or merge request description.

## Core Workflow

1. Determine the source material:
    - Current local changes.
    - A branch compared with a base branch.
    - A provided diff, commit list, issue, or existing PR/MR draft.
2. If deriving from a repository, inspect only the smallest useful change set:
    - Run `git status --short` first.
    - If using current local changes, inspect `git diff --stat`, `git diff`,
      `git diff --cached --stat`, and `git diff --cached` as needed.
    - If using a branch comparison, identify the base branch, then inspect
      `git diff --stat <base>...HEAD`, `git diff <base>...HEAD`, and
      `git log --oneline <base>..HEAD` as needed.
3. Summarize the problem the user encounters that this change addresses before
   describing the implementation.
4. Draft the PR/MR message using the standard template unless the repository
   provides its own template.
5. Include validation only when it was actually run or explicitly provided. If
   no validation information is available, include a placeholder such as
   `Not run (reason not provided)`.
6. Call out risks, migrations, rollout notes, screenshots, or follow-up work
   when they are relevant to reviewing or merging the change.

## Standard Template

```markdown
## Summary

<One or two sentences describing what this change does.>

## Motivation

<Why this change is needed, what problem it solves, or what context led to it.>

## Modifications

- <Concrete implementation change>
- <Concrete implementation change>
- <Concrete implementation change>

## Result

<What is different after this change lands. Describe user-visible, developer-facing, or operational impact.>

## Validation

- <Command, test, manual check, or "Not run" with a short reason>
```

Optional sections:

```markdown
## Screenshots

<Before/after images or a note that screenshots are not applicable.>

## Risks and Rollout

- <Compatibility, migration, deployment, or rollback notes>

## Follow-ups

- <Known remaining work that is intentionally out of scope>
```

## Drafting Rules

- Prefer `Summary` over a one-line placeholder at the top. It gives reviewers
  an immediate answer before they read context.
- Use `Motivation` for the "why", not an implementation recap.
- Use `Modifications` for reviewable facts from the diff.
- Use `Result` for behavior, workflow, API, or documentation impact after the
  change is merged.
- Use `Validation` for tests and checks. Do not mix validation into `Result`.
- Keep bullets specific and parallel. Start each bullet with an active verb
  when it reads naturally.
- Do not invent issue IDs, benchmarks, screenshots, tests, approvals, or user
  impact.
- If information is missing, write a clear placeholder such as
  `Not run (reason not provided)` rather than pretending the check happened.
- Keep the final message concise enough for reviewers to scan.

## Output Guidance

- Provide a complete copy-ready PR/MR description.
- If the user asks for feedback on a template, briefly explain improvements
  before giving the revised template.
- If there are multiple reasonable levels of detail, default to the shorter
  version and include only review-critical context.
- Mention any assumptions made from the diff or provided context.

## Reference

For examples and template variants, read `references/template.md` only when the
task needs additional examples or a different PR/MR style.
