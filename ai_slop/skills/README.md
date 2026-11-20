# Skills

Put each skill in its own directory:

```text
skills/<skill-name>/SKILL.md
```

Supporting files (scripts, references, templates) belong beside `SKILL.md`.
After adding or changing a skill, run `../sync.sh` to link it into
`~/.agents/skills/<skill-name>` and `~/.claude/skills/<skill-name>`.

Existing tool-managed skills are not touched; `sync.sh` links individual skill
folders rather than replacing the whole skills directory.
