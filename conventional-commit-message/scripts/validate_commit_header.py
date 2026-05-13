#!/usr/bin/env python3
"""Validate an opinionated Conventional Commit header."""

import re
import sys


TYPES = (
    "feat",
    "fix",
    "refactor",
    "perf",
    "style",
    "test",
    "docs",
    "build",
    "ops",
    "chore",
)

HEADER_RE = re.compile(
    rf"^({'|'.join(TYPES)})(\(([^()\n]+)\))?(!)?: ([^\n.].*[^\n.]|[^\n.])$"
)
MERGE_RE = re.compile(r"^Merge branch '.+'$")
REVERT_RE = re.compile(r'^Revert ".+"$')


def validate(header: str) -> list[str]:
    if MERGE_RE.match(header) or REVERT_RE.match(header):
        return []

    match = HEADER_RE.match(header)
    errors: list[str] = []

    if not match:
        errors.append(
            "header must be '<type>(<optional scope>)<optional !>: <description>'"
        )
        return errors

    scope = match.group(3)
    description = match.group(5)

    if scope and re.search(r"(#\d+|[A-Z]+-\d+)", scope):
        errors.append("scope must not be an issue identifier")

    if description[0].isupper():
        errors.append("description must start with a lowercase letter")

    if description.endswith("."):
        errors.append("description must not end with a period")

    return errors


def main() -> int:
    if len(sys.argv) > 1:
        header = " ".join(sys.argv[1:]).strip()
    else:
        header = sys.stdin.read().strip()

    if not header:
        print("missing commit header", file=sys.stderr)
        return 2

    errors = validate(header)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
