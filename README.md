# Code Skills

A collection of skills for AI coding agents. Skills are packaged instructions,
scripts, and reference material that extend an agent's capabilities for common
software engineering workflows.

Skills in this repository follow the [Agent Skills](https://agentskills.io/)
format.

[![skills.sh](https://skills.sh/b/ankitgoyalio/code-skills)](https://skills.sh/ankitgoyalio/code-skills)

## Available Skills

### conventional-commit-message

Create, validate, rewrite, and explain Git commit messages using an opinionated
Conventional Commits format. The skill can stage repository changes, inspect the
staged diff, derive a commit message, validate the header, and create exactly
one commit.

**Use when:**

- Committing current repository changes
- Validating an existing commit message
- Rewriting a commit message to match Conventional Commits
- Explaining why a commit message does or does not satisfy the local convention

**Covers:**

- Typed Conventional Commit headers
- Optional scopes and breaking-change markers
- Body and footer guidance
- Issue footer placement
- Merge, revert, and initial commit special cases
- Optional deterministic header validation with Python 3

**Included files:**

- [SKILL.md](conventional-commit-message/SKILL.md) - agent instructions and workflow
- [scripts/validate_commit_header.py](conventional-commit-message/scripts/validate_commit_header.py) - header validator
- [references/convention.md](conventional-commit-message/references/convention.md) - detailed examples and versioning notes

### pull-request-message

Draft, improve, rewrite, and review pull request or merge request descriptions
from repository changes, branch diffs, commit lists, provided patches, or
existing drafts. The skill uses an opinionated template that separates summary,
motivation, modifications, result, and validation.

**Use when:**

- Drafting a PR or MR description from local changes
- Improving an existing PR or MR message
- Turning a diff, branch, or commit list into reviewer-friendly context
- Reviewing whether a PR/MR template has the right sections

**Covers:**

- Diff and commit inspection guidance
- Motivation, implementation, result, and validation separation
- Optional screenshots, risks, rollout, and follow-up sections
- Copy-ready output guidance
- Template variants for documentation-only and small changes

**Included files:**

- [SKILL.md](pull-request-message/SKILL.md) - agent instructions and workflow
- [references/template.md](pull-request-message/references/template.md) - template variants and examples

## Installation

Install this skill collection with the Agent Skills CLI:

```bash
npx skills add ankitgoyalio/code-skills
```

## Usage

Skills are automatically available once installed. The agent will load the full
skill instructions only when a relevant task is detected.

Examples:

```text
Commit my changes
```

```text
Validate this commit message: feat(api): add user search
```

```text
Rewrite this commit message using our convention
```

```text
Draft a pull request message from my current changes
```

```text
Improve this merge request description
```

## Skill Structure

Each skill directory contains:

- `SKILL.md` - required instructions and metadata for the agent
- `scripts/` - optional helper scripts for deterministic checks or automation
- `references/` - optional supporting documentation loaded only when needed

Keep `SKILL.md` focused and move detailed examples, long rule lists, and
background material into `references/` so agents can use context efficiently.

## Contributing

When adding or changing a skill, update this README in the same change so the
skill catalog, installation notes, and usage examples stay accurate.

## License

MIT
