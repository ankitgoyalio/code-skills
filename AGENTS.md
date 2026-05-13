# AGENTS.md

This file provides guidance to AI coding agents when working in this repository.

## Repository Overview

This repository is a collection of skills for AI coding agents. Each skill is a
directory containing packaged instructions, optional scripts, and optional
reference material that extend agent behavior for a specific workflow.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Mandatory README Maintenance

Whenever you make any repository change, check whether `README.md` needs to be
updated. Update it in the same change when you:

- Add, remove, rename, or materially change a skill.
- Change a skill description, trigger behavior, or expected use case.
- Add, remove, rename, or materially change files under `scripts/` or
  `references/`.
- Change installation, usage, compatibility, license, or repository structure.

The README is the public skill catalog. Do not leave it stale after changing
the repo.

## Skill Directory Structure

Use one top-level directory per skill:

```text
{skill-name}/
  SKILL.md
  scripts/
    {script_name}.py
  references/
    {reference-name}.md
```

`scripts/` and `references/` are optional, but `SKILL.md` is required.

## Naming Conventions

- Skill directories use `kebab-case`, such as `conventional-commit-message`.
- `SKILL.md` is always uppercase and must use this exact filename.
- Markdown references use clear lowercase names, preferably `kebab-case`.
- Script names should be descriptive and consistent with the language's normal
  conventions. Existing Python scripts use `snake_case.py`.

## SKILL.md Format

Start every skill with YAML front matter:

```markdown
---
name: {skill-name}
description: {One or two sentences describing when the agent should use this skill.}
compatibility: {Optional runtime or platform notes.}
---
```

Then include focused operational guidance for the agent:

- When to use the skill.
- The workflow the agent should follow.
- Required commands or helper scripts.
- Output guidance for presenting results to the user.
- Links to supporting files in `references/` only when the task needs them.

## Context Efficiency

Skills are loaded on demand. Keep the startup metadata specific and keep full
instructions concise.

- Keep `SKILL.md` focused on execution, not exhaustive background.
- Move long examples, detailed rules, and edge cases into `references/`.
- Prefer helper scripts for deterministic checks and repeatable automation.
- Link directly to supporting files from `SKILL.md` so agents can load only the
  context they need.

## Script Guidance

When adding scripts:

- Use the most appropriate runtime for the task and document any requirement in
  the skill front matter or README.
- Include a shebang when the script is intended to be executed directly.
- Fail clearly on invalid input.
- Write human-readable errors to stderr.
- Keep stdout suitable for the caller to parse or summarize.
- Avoid network access unless the skill explicitly requires it.

## Updating Existing Skills

When modifying a skill:

1. Read the current `SKILL.md` and any directly referenced files first.
2. Keep changes scoped to the skill's stated purpose.
3. Update or add scripts only when they make the workflow more deterministic.
4. Update references when rules, examples, or compatibility notes change.
5. Update `README.md` if the public catalog entry or installation/usage
   guidance changed.

## Validation

Run the narrowest useful validation for the change. For documentation-only
changes, at minimum review the rendered Markdown structure and confirm links and
paths are accurate. For script changes, run the script with representative valid
and invalid input.
