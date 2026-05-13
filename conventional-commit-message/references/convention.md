# Conventional Commit Message Reference

This reference captures the opinionated convention used by the skill. It stays
within the Conventional Commits specification.

## Formats

General commit:

```text
<type>(<optional scope>): <description>

<optional body>

<optional footer>
```

Breaking change:

```text
<type>(<optional scope>)!: <description>

<optional body>

BREAKING CHANGE: <description, justification, and migration note>
```

Initial commit:

```text
chore: init
```

Merge commit:

```text
Merge branch '<branch name>'
```

Revert commit:

```text
Revert "<reverted commit subject line>"
```

## Type Selection

- `feat`: API or UI feature added, adjusted, or removed.
- `fix`: API or UI bug fixed.
- `refactor`: code rewritten or restructured without API or UI behavior change.
- `perf`: performance-focused refactor.
- `style`: formatting, whitespace, semicolons, or code style only.
- `test`: missing tests added or existing tests corrected.
- `docs`: documentation-only change.
- `build`: build tools, dependencies, project version, or packaging.
- `ops`: infrastructure, deployment scripts, CI/CD, backups, monitoring, or
  recovery.
- `chore`: repository maintenance, init commits, `.gitignore`, or similar
  housekeeping.

## Scope Selection

The scope provides additional project-specific context.

Good scopes:

- package names
- app or service names
- modules
- components
- public API areas
- meaningful directories when no better domain scope exists

Avoid:

- issue IDs such as `#123` or `JIRA-456`
- overly broad scopes such as `app` when a clearer component exists
- scopes that repeat the type

## Description Checklist

- Mandatory.
- Imperative and present tense.
- Lowercase first letter.
- No final period.
- Concise enough to scan in history.
- Reads naturally after "This commit will..." or "This commit should..."

## Body Checklist

Use a body when the change has non-obvious motivation, migration implications,
or important previous behavior.

- State why the change is needed.
- Contrast with previous behavior.
- Keep line lengths readable.
- Avoid repeating the header.

## Footer Checklist

Use the footer for issue references and breaking-change notes.

Examples:

```text
Closes #123
```

```text
Fixes JIRA-456
```

```text
BREAKING CHANGE: ticket endpoints no longer support listing all entities.
```

For multi-line breaking changes:

```text
BREAKING CHANGE:

The ticket list endpoint has been removed.

Use the paginated search endpoint instead.
```

## Versioning Notes

When commit messages drive versioning:

- Breaking changes increment the major version.
- API-relevant `feat` or `fix` commits increment the minor version.
- Other commits increment the patch version.

## Examples

```text
feat: add email notifications on new direct messages
```

```text
feat(shopping cart): add the amazing button
```

```text
feat!: remove ticket list endpoint

Refers to JIRA-1337.

BREAKING CHANGE: ticket endpoints no longer support listing all entities.
```

```text
fix(shopping-cart): prevent ordering an empty shopping cart
```

```text
fix(api): fix wrong calculation of request body checksum
```

```text
fix: add missing parameter to service call

The error occurred because the caller omitted the tenant identifier.
```

```text
perf: decrease memory footprint for unique visitor calculation
```

```text
build: update dependencies
```

```text
build(release): bump version to 1.0.0
```

```text
refactor: implement fibonacci number calculation as recursion
```

```text
style: remove empty line
```
