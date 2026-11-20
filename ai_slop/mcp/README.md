# MCP servers

Nothing is synced here yet.

When MCPs are added, prefer a small list of native commands over maintaining
three config formats by hand:

```bash
opencode mcp add <name> --global ...
claude mcp add --scope user ...
codex mcp add ...
```

Each command writes to the harness's own config and preserves unrelated settings:

- OpenCode: global `opencode.json` / `opencode.jsonc`
- Claude Code: user scope in `~/.claude.json`
- Codex: `[mcp_servers.<name>]` in `~/.codex/config.toml`

Keep secrets in environment variables and use the harness's variable syntax
(for example `{env:VAR}` for OpenCode) rather than committing them.
