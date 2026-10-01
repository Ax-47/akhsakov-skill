#!/usr/bin/env python3
"""Check that every <skill>/SKILL.md has valid frontmatter."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def check(path):
    errors = []
    fields = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fields is None:
        return ["missing or unterminated frontmatter"]
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_RE.match(name):
        errors.append(f"name {name!r} must be lowercase words joined by hyphens")
    elif name != path.parent.name:
        errors.append(f"name {name!r} does not match folder {path.parent.name!r}")
    if not description:
        errors.append("description is empty")
    elif len(description) > 1024:
        errors.append(f"description is {len(description)} chars (max 1024)")
    return errors


def main():
    skills = sorted(ROOT.glob("*/SKILL.md"))
    if not skills:
        print("no skills found")
        return 1
    failed = False
    for path in skills:
        errors = check(path)
        rel = path.relative_to(ROOT)
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {rel}: {error}")
        else:
            print(f"ok   {rel}")
    if (ROOT / "SKILL.md").exists():
        failed = True
        print("FAIL SKILL.md: skills belong in their own folder, not the repo root")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
