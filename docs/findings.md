# Research findings

## 2026-08-26 — Initial setup

### Confirmed from project-provided command documentation

Kana exposes a cultivation/progression game through commands such as `.tuluyen`, `.dotpha`, `.bicanh`, `.danhboss`, `.taoboss`, `.nhiemvu`, garden commands, sect/social commands, and higher-realm progression commands.

Known cooldowns from the supplied command list include 60s for `.tuluyen`, 5m for `.pvp`, 30s for `.danhboss`, 1h for `.bicanh`, 1.5h for `.truyenthua`, 15m for `.linhngo`, and 2h for `.vandinh thi`.

### Not yet confirmed

- Public API or SDK
- Response payload/schema
- Whether commands are handled by plain messages, interactions, or another supported interface
- Exact success/failure response markers
- Server-side cooldown response format
- Boss state representation
- Account/session mechanism suitable for an authorized client

Do not turn assumptions into implementation details. Each protocol fact should be marked as observed/confirmed when collected.
