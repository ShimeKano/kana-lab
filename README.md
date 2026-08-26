# Kana Lab

A safe research and development workspace for building a Kana automation client from documented/authorized interfaces.

## Goals

- Map Kana commands and observed responses.
- Build a transport-independent Kana adapter.
- Reuse proven automation architecture patterns: scheduling, cooldowns, state, queues, parsing, and modular actions.
- Keep secrets out of source control.
- Separate observations from assumptions.

## Project layout

```text
kana-lab/
├── docs/
│   ├── commands.md
│   ├── findings.md
│   └── protocol.md
├── experiments/
│   ├── command_probe/
│   ├── response_parser/
│   └── timing/
├── kana/
│   ├── client.py
│   ├── models.py
│   └── parser.py
├── tests/
└── .gitignore
```

## Safety

Do not commit account tokens, cookies, passwords, or session credentials. The project is intended to use supported/authorized interfaces and normal bot interactions; it does not implement authentication bypass, CAPTCHA bypass, or stealth/evasion mechanisms.
