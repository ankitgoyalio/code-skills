# Code Skills

A collection of skills for AI coding agents. Skills are packaged instructions,
scripts, and reference material that extend an agent's capabilities for common
software engineering workflows.

Skills in this repository follow the [Agent Skills](https://agentskills.io/)
format.

[![skills.sh](https://skills.sh/b/ankitgoyalio/code-skills)](https://skills.sh/ankitgoyalio/code-skills)

## Available Skills

### coderabbit-code-review

Run detailed CodeRabbit-powered code reviews for local diffs, branches, pull
requests, or specific repository directories. The skill checks CLI
prerequisites, selects an appropriate review scope, captures CodeRabbit's
plain-text output to a report file, and presents human-readable findings in
review form.

**Use when:**

- Reviewing local code changes or branch changes
- Running CodeRabbit on a repository or specific directory
- Checking code quality, security, performance, or bug risk
- Summarizing CodeRabbit findings for a pull request
- Fixing actionable issues reported by CodeRabbit

**Covers:**

- CodeRabbit CLI and authentication checks
- Working tree, committed, base branch, and base commit review scopes
- `--dir` reviews for specific Git repositories
- Plain-text detailed review output by default, with `--agent` reserved for
  explicit machine-readable workflows
- Full review capture to a text artifact before summarization to avoid
  truncated terminal streams
- Severity-based findings with code-review output guidance
- Safety notes for secret exposure, authentication tokens, and untrusted output

**Included files:**

- [SKILL.md](coderabbit-code-review/SKILL.md) - agent instructions and workflow

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

### kiss-dry-code-review

Review unmerged branch changes against the repository default branch for KISS
and DRY issues. The skill focuses on overcomplicated code, unnecessary
abstraction, duplicated changing knowledge, and repeated implementation details
that can drift before a branch is merged.

**Use when:**

- Reviewing branch or pull request changes for KISS and DRY concerns
- Checking unmerged changes against the repository default branch
- Finding over-engineered code, avoidable indirection, or premature abstraction
- Finding duplicated business rules, mappings, constants, validations, or test
  setup
- Producing a maintainability-focused code review with actionable fixes

**Covers:**

- Git-based default branch discovery or an explicit base branch
- KISS checks for unnecessary complexity, control flow, public surface area,
  configuration, and test setup
- DRY checks for duplicated change-prone knowledge across code, tests, schemas,
  build logic, and documentation
- Guardrails against recommending premature abstraction when local duplication
  is clearer
- Separate KISS and DRY passes for large or risky diffs
- Validation and prioritization guidance to reduce speculative findings
- Severity-based review output with file and line references

**Included files:**

- [SKILL.md](kiss-dry-code-review/SKILL.md) - agent instructions and workflow

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

### coderabbit-code-review examples

```text
Run a detailed CodeRabbit review of my uncommitted changes and summarize the captured report
```

```text
Run a detailed CodeRabbit review of this branch compared with main and include the report file path
```

```text
Run CodeRabbit against ~/Developer/fsm-ios and give me a human-readable review from the saved report
```

### conventional-commit-message examples

```text
Commit my changes
```

```text
Validate this commit message: feat(api): add user search
```

```text
Rewrite this commit message using our convention
```

### kiss-dry-code-review examples

```text
Review my unmerged changes for KISS and DRY issues
```

```text
Check this branch for over-engineering and duplicated logic before I open a PR
```

### pull-request-message examples

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
