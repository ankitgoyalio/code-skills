---
name: conventional-commit-message
description: Stage all current Git changes and create exactly one commit using this repository's opinionated Conventional Commits workflow, including deterministic header validation and breaking-change handling. Use when asked to commit changes or to validate, rewrite, or explain a commit message against this convention.
---

# Conventional Commit Message

## Core Workflow

1. Determine the task:
    - Commit repository changes.
    - Validate an existing message.
    - Rewrite a message to match the convention.
2. If committing repository changes, stage all current changes first:
    - Run `git add -A`.
    - Inspect the staged result with `git diff --cached --stat` and
      `git diff --cached`.
    - If nothing is staged after `git add -A`, report that there are no changes
      to commit.
3. Derive the commit message from the staged diff unless the user provided a
   full message.
4. Validate the header before committing. Use the Python 3 helper
   `scripts/validate_commit_header.py` when a deterministic check is useful.
5. Create exactly one commit with the validated message.
6. Do not run tests, lint, build, or type checks unless the user explicitly
   asks for them.

## Message Format

```text
<type>(<optional scope>)<optional !>: <description>

<optional body>

<optional footer>
```

The command form is:

```shell
git commit -m"<header>" -m"<optional body>" -m"<optional footer>"
```

## Header Rules

- `type` is mandatory.
- `description` is mandatory.
- `scope` is optional and project-defined.
- Do not use issue identifiers as scopes.
- Use imperative, present tense: `change`, not `changed` or `changes`.
- Start the description with a lowercase letter.
- Do not end the description with a period.
- Use `!` before `:` when the commit introduces a breaking change.

Allowed types:

- `feat`: API or UI feature added, adjusted, or removed.
- `fix`: API or UI bug fixed.
- `refactor`: code rewritten or restructured without API or UI behavior change.
- `perf`: performance-focused refactor.
- `style`: code style only, with no behavior change.
- `test`: missing tests added or existing tests corrected.
- `docs`: documentation-only changes.
- `build`: build tools, dependencies, project version, or packaging.
- `ops`: infrastructure, deployment, CI/CD, backups, monitoring, or recovery.
- `chore`: maintenance tasks such as init commits or `.gitignore` updates.

Special cases:

- Initial commit: `chore: init`
- Merge commit: keep Git's default `Merge branch '<branch name>'`
- Revert commit: keep Git's default `Revert "<reverted commit subject line>"`

## Body Rules

The body is optional. Include it when the header alone does not explain the
motivation or when previous behavior matters.

- Use imperative, present tense.
- Explain the motivation for the change.
- Contrast the change with previous behavior.
- Keep lines readable in common Git tools.

## Footer Rules

The footer is optional except for breaking changes.

- Use issue references when useful, such as `Closes #123` or `Fixes JIRA-456`.
- Put issue references in the footer, not in the scope.
- Breaking changes must start with `BREAKING CHANGE:`.
- For a single-line breaking-change note, continue after the colon.
- For a multi-line breaking-change note, put a blank line after
  `BREAKING CHANGE:`.

When a commit has a breaking change, prefer both:

```text
feat(api)!: remove status endpoint

BREAKING CHANGE: status endpoint is no longer available.
```

## Commit Guidance

- Use multiple `-m` arguments for multi-paragraph messages:

```shell
git commit -m"<header>" -m"<optional body>" -m"<optional footer>"
```

- If the user provides a complete commit message, use it exactly after
  validation.
- If the user provides only a type or `type(scope)`, keep that prefix and derive
  the description, body, and footer from the staged diff.
- If validation fails for a user-provided message, explain the specific rule
  violations and do not commit until the message is corrected or a valid
  replacement is derived.

## Output Guidance

- After a successful commit, report the commit hash and final commit message.
- If validation fails, list the specific rule violations and provide a corrected
  message.
- If multiple messages are plausible, provide up to three options with distinct
  type or scope choices only when not committing automatically.
- Do not invent issue IDs. Include issue footers only when the user provides
  them or the repository context makes them clear.

## Reference

For detailed examples and versioning notes, read
`references/convention.md` only when the task needs extra guidance.
