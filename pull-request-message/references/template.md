# Pull Request Message Templates

## Default

```markdown
## Summary

<One or two sentences describing what this change does.>

## Motivation

<Explain the context, the problem, and why the change is needed.>

## Modifications

- <Describe one concrete change>
- <Describe one concrete change>
- <Describe one concrete change>

## Result

<Describe what changes after merge for users, developers, operators, or documentation readers.>

## Validation

- <Test command or manual check>
```

## Documentation-Only Change

```markdown
## Summary

<One or two sentences describing the documentation update.>

## Motivation

<Explain what was unclear, missing, stale, or hard to discover.>

## Modifications

- <Describe the documentation change>
- <Describe any catalog, examples, or reference updates>

## Result

<Describe what readers or maintainers can now understand or do.>

## Validation

- Reviewed rendered Markdown structure and verified links/paths.
```

## Small Change

```markdown
## Summary

<One or two sentences describing the change.>

## Validation

- <Test command, manual check, or "Not run" with reason>
```

Use this shorter version only when the change is straightforward and the
motivation is obvious from the summary.

## Review Checklist Variant

```markdown
## Summary

<One or two sentences describing what this change does.>

## Motivation

<Why this change is needed.>

## Modifications

- <Concrete implementation change>
- <Concrete implementation change>

## Result

<Expected impact after merge.>

## Validation

- <Command or manual check>

## Reviewer Notes

- [ ] <Specific area where reviewer attention is useful>
- [ ] <Compatibility, migration, or rollout concern to verify>
```

Use reviewer notes only when there is a concrete area where targeted reviewer
attention would reduce risk.
