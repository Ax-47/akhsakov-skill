# akhsakov-skill

Personal [Claude skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) with a cute cat theme.

## Skills

| Skill | What it does |
| --- | --- |
| [mika-chan](mika-chan/SKILL.md) | Claude chats as Mika-chan (มิกะจัง), a cheerful helper who ends sentences with เนี๊ยน / nya and uses kaomoji, while keeping answers accurate and files, code and outgoing messages in their normal style. |
| [nyantify](nyantify/SKILL.md) | `/nyantify <text>` rewrites text into cat-speak (เนี๊ยน for Thai, nya/nyan for English) with varied kaomoji, leaving meaning, structure and code untouched. |

## Layout

Each skill lives in its own folder:

```
<skill-name>/
  SKILL.md   # frontmatter (name, description) + instructions
```

The `name` in the frontmatter must match the folder name.

## Installing

- **Claude.ai / Claude Desktop:** zip a skill folder (e.g. `nyantify/`) and upload it under Settings → Capabilities → Skills.
- **Claude Code:** copy a skill folder into `~/.claude/skills/` (personal) or `.claude/skills/` in a project.

## Adding a skill

1. Create `<skill-name>/SKILL.md` with `name` and `description` frontmatter.
2. Add a row to the table above.
3. Run `python scripts/validate_skills.py` — CI runs the same check on every push and pull request.
