---
name: maintainability-code-review
description: Review unmerged branch changes against the repository default branch for maintainability issues involving simplicity, duplication, and Boolean design. Use when asked to find overcomplicated code, unnecessary abstraction, repeated knowledge, ambiguous Boolean names, opaque Boolean parameters, or other maintainability problems in changes that have not merged yet.
compatibility: Requires Git when deriving review findings from local repository changes.
---

# Maintainability Code Review

Use this skill when the user asks to review branch, pull request, or unmerged
changes for KISS (Keep it simple, stupid), DRY (Don't repeat yourself), and
Boolean design issues.

## Principles

- KISS: treat simplicity as a design goal. Flag solutions that are harder to
  read, test, reason about, operate, or repair than the changed behavior
  requires.
- DRY: every piece of changing knowledge should have one clear, authoritative
  representation. Flag repeated business rules, mappings, constants, schemas,
  validations, queries, test setup, build logic, or documentation that are
  likely to drift.
- Balance the two principles. Do not recommend abstraction only because code is
  textually similar; prefer duplication over the wrong abstraction when the
  repeated code has different reasons to change.
- Boolean design: treat a Boolean as the answer to one clear yes-or-no
  question. Prefer names and APIs that make the question and the meaning of
  each value evident at the use site.

## Core Workflow

1. Determine the review scope:
    - Use the user's explicit base branch when provided.
    - Otherwise discover the repository's default branch using Git before
      comparing changes.
2. Confirm the target directory is a Git repository:

```shell
git rev-parse --is-inside-work-tree
```

3. Discover the default branch when the user did not provide a base:

```shell
git symbolic-ref --quiet --short refs/remotes/origin/HEAD
git remote show origin
```

Prefer the `refs/remotes/origin/HEAD` result when available, removing the
`origin/` prefix only for local branch checks. If the remote default branch is
not configured, inspect local branches and ask for a base branch only when no
reasonable base can be inferred.

4. Inspect the smallest useful branch context:

```shell
git status --short
git branch --show-current
git diff --stat <base>...HEAD
git log --oneline <base>..HEAD
```

Use the selected base exactly in comparison commands. Examples include
`origin/main`, `origin/master`, `main`, `master`, or a user-provided release
branch.

5. Read the relevant diff and files before reporting findings:

```shell
git diff <base>...HEAD
```

For large diffs, inspect `git diff --name-only <base>...HEAD` first, then read
only files needed to verify KISS or DRY concerns.

6. Understand the changed behavior before judging the implementation. For each
   candidate finding, ask how the branch works, how it can fail, and whether the
   simpler or less duplicated alternative preserves the intended behavior.
7. Make a Boolean pass over changed declarations and call sites. Check names,
   polarity, responsibilities, and whether Boolean arguments hide modes or
   materially different behavior.
8. For large or risky diffs, make separate KISS, DRY, and Boolean passes before
   synthesizing the final review. Keep notes independent until all passes are
   complete so early findings do not bias later checks.
9. Identify only issues introduced or materially worsened by the unmerged
   changes. Do not report pre-existing complexity unless the branch depends on
   it or makes it worse.
10. Validate findings against the actual code before reporting them. Re-read the
   relevant surrounding code, tests, or call sites to rule out false positives.
11. Prefer concrete fixes over broad advice. Tie each finding to the changed
    behavior, the duplicated knowledge, or the unnecessary complexity.
12. Prioritize findings by impact. Report critical and warning issues first;
    include low-value info findings only when they are clearly actionable.

## What To Flag

KISS issues:

- Layers, indirection, configuration, generic helpers, or abstractions that do
  not simplify the current requirement.
- Complex control flow, state handling, branching, or error paths that can be
  expressed more directly.
- New public API surface, options, flags, or extension points without a clear
  need in the branch.
- Over-engineered test setup or fixtures that make the behavior harder to
  verify than a direct test would.

DRY issues:

- Repeated source-of-truth values such as enum lists, route names, field names,
  permissions, feature flags, status mappings, validation rules, or constants.
- Copy-pasted code blocks where a bug fix or behavior change would need to be
  made in multiple unrelated places.
- Parallel test expectations, fixtures, docs, generated artifacts, or schema
  definitions that duplicate change-prone knowledge.
- Repeated transformations or conditional rules that should share a named
  helper, table, data structure, or existing local abstraction.

Boolean issues:

- Ambiguous names such as `flag`, `done`, `status`, or `check` that do not state
  the question being answered. Prefer a specific, grammatical question; common
  prefixes are `is` for state or identity, `has` for possession or presence,
  `can` for capability, and `should` for intent or a decision.
- Prefixes that do not match the question, such as `isAccess`, `hasActive`, or
  `canAdmin`. Apply naming conventions idiomatically for the project language;
  do not require these exact prefixes when another form is clearer and
  conventional.
- Negative names that create confusing negation, such as `isNotEnabled`,
  `hasNoAccess`, or `!isDisabled`. Prefer positive polarity, except when
  faithfully representing an external API or protocol; map negative external
  fields to positive domain concepts at the boundary when practical.
- A Boolean that combines multiple independent facts under a vague name or is
  reused for different stages of a workflow. Prefer explicit predicates, early
  returns, or a result/state type that preserves the distinctions.
- Positional Boolean arguments whose meaning is unclear at the call site,
  especially multiple Booleans or a Boolean that selects substantially
  different behavior. Prefer separate methods, a named enum/mode, or an options
  object according to the number and nature of the choices.

Do not flag:

- Small local duplication that is clearer than a premature abstraction.
- Similar code that changes for different business reasons.
- Verbose code that is required by framework conventions, compatibility, type
  safety, accessibility, security, or observability.
- Clear Boolean names that follow the language or repository convention even
  when they do not use `is`, `has`, `can`, or `should`.
- A single self-evident Boolean argument when replacing it would add more
  ceremony without improving the call site.
- Large unchanged files that merely appear in the diff due to formatting or
  generation, unless the branch changed the generated source of truth.

## Output Guidance

Use a code-review response shape:

1. Findings first, ordered by severity.
2. Include file and line references whenever possible.
3. Label each finding as `KISS`, `DRY`, `BOOLEAN`, or a slash-separated
   combination when it spans concerns.
4. Explain why the issue matters for future change, readability, testing, or
   defect risk.
5. Suggest the smallest practical fix.
6. Distinguish confirmed issues from open questions. Do not present speculative
   concerns as findings.
7. If the branch appears misguided because of repeated critical or warning
   KISS, DRY, or Boolean issues, say that directly and explain the simpler
   direction.
8. If no issues are found, say that clearly and include the base comparison
   that was reviewed.
9. Keep summaries brief and secondary to actionable findings.

Severity mapping:

- Critical: duplicated or overcomplicated logic likely to cause incorrect
  behavior, security impact, data loss, or serious production risk.
- Warning: complexity or duplication likely to cause drift, defects, or
  meaningfully harder maintenance.
- Info: minor simplification or consolidation opportunities with low immediate
  risk.
