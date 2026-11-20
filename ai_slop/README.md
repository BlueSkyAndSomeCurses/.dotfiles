# ai_slop

Portable, per-user AI harness setup shared through this dotfiles repo.

It keeps always-on rules in small source files, generates one `AGENTS.md`, and
links that file into every harness. Skills are linked one folder at a time. No
root, and no dependency beyond Bash, `ln`, `mkdir`, `cmp`, and standard Unix
tools.

## Install

From anywhere:

```bash
~/Documents/.dotfiles/ai_slop/sync.sh
```

On a new machine, after cloning the dotfiles:

```bash
git clone <dotfiles-url> ~/Documents/.dotfiles
~/Documents/.dotfiles/ai_slop/sync.sh
```

Run the same command after `git pull`, or after moving the repo.

## Check

`--check` reports stale generated output and missing or incorrect links without
changing anything:

```bash
~/Documents/.dotfiles/ai_slop/sync.sh --check
```

It exits `1` when something needs syncing, so it can be used in a shell prompt or
CI.

## Layout

```text
ai_slop/
├── AGENTS.md          # generated: all rules, do not edit directly
├── rules/
│   ├── 00-communication.md
│   ├── 05-cognitive-load.md
│   ├── 10-code.md
│   └── 20-prose.md
├── skills/
│   └── ste/
│       └── SKILL.md   # full STE rules, loaded on demand
├── mcp/               # notes for future MCP setup
└── sync.sh            # the one command
```

## Editing rules

Edit the files in `rules/`, then run `sync.sh`. The files are concatenated in
filename order into `AGENTS.md`, with a generated-file header.

Use the numeric prefixes to control order. Add `30-something.md` to append a new
block.

Do not use `@import` in `AGENTS.md`. Claude Code supports imports, but Codex and
OpenCode do not. One generated file gives every harness the same content.

Splitting always-on rules into imported files does not save context: imports load
at session start too. Keep this file short. Put long or optional material in a
skill so it loads only when needed. The `ste` skill is the example: the global
rules say to use STE, and the full checklist loads only when writing docs.

## What gets linked

| Harness | Instructions | Skills |
|---|---|---|
| OpenCode | `${XDG_CONFIG_HOME:-~/.config}/opencode/AGENTS.md` → `AGENTS.md` | `~/.agents/skills/<name>` → `skills/<name>` |
| Claude Code | `~/.claude/CLAUDE.md` → `AGENTS.md` | `~/.claude/skills/<name>` → `skills/<name>` |
| Codex | `~/.codex/AGENTS.md` → `AGENTS.md` | `~/.agents/skills/<name>` → `skills/<name>` |
| OpenResearch | inherits the harness it launches | inherits the harness it launches |

OpenCode also reads `~/.claude/skills`, so the same skill is visible there
without a separate link.

OpenResearch does not keep a separate global `AGENTS.md`. It launches Claude
Code, Codex, or OpenCode with its own playbook, so the personal instructions and
skills above are inherited automatically. Do not replace
`~/.config/opencode/skills` wholesale: orx manages its own `orx` skill shim
there. `sync.sh` only links individual skills under `~/.agents/skills` and
`~/.claude/skills`.

## Adding skills

Create a normal Agent Skills folder:

```text
ai_slop/skills/my-skill/
└── SKILL.md
```

Then rerun `sync.sh`. The skill becomes available to OpenCode, Claude Code, and
Codex on every project. Existing tool-managed skills are left alone.

## MCPs

Not synced yet. When you add them, prefer the harnesses' own commands over
hand-merging JSON and TOML:

```bash
opencode mcp add <name> --global ...
claude mcp add --scope user ...
codex mcp add ...
```

That preserves unrelated settings in `opencode.json`, `~/.claude.json`, and
`~/.codex/config.toml`. Keep secrets in environment variables and reference them
from the config; never commit them. See `mcp/README.md`.

## Safety

- Existing real files are moved to `~/.ai-slop-backups/<timestamp>/` before a
  symlink replaces them.
- `AGENTS.md` is rebuilt from `rules/` on every run; edit the source files.
- `settings.json`, `~/.claude.json`, `opencode.json`, and
  `~/.codex/config.toml` are never touched.
- Codex's `~/.codex/AGENTS.override.md`, if present, takes precedence over
  `~/.codex/AGENTS.md`; `sync.sh` prints a warning when it sees one.
- Links are absolute. If the dotfiles repo moves, rerun `sync.sh`.

## Why not exuno?

Exuno is useful for a repository that needs the same rules in many tool-specific
formats. This setup is per-user global config, and the instruction format is
already shared: `AGENTS.md` plus one `CLAUDE.md` path. Symlinks and one small
generation step solve that with no binary and no extra sync layer. MCPs can be
added later with the native CLI commands above.
