# Kana Lab

A safe research and development workspace for building a Kana automation client from documented/authorized interfaces.

## Current phase: Discord Observer

Kana Lab can now run as a **read-only Discord observer** using a normal Discord bot token. Give it a channel ID and it records message creation, edits, deletes, embeds, components, attachments, and references as JSONL.

### Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set the values in `.env`:

```env
DISCORD_BOT_TOKEN=your_bot_token
OBSERVE_CHANNEL_ID=123456789012345678
DATA_DIR=./observations/runtime
```

Then run:

```bash
python -m kana.discord_observer
```

The observer writes to `observations/runtime/events.jsonl` and does not commit runtime data to the repository.

> The bot must be able to view the target channel. Because the observer reads message content, enable Discord's **Message Content Intent** for the bot in the Discord Developer Portal and in the application configuration. No user/self-bot token is supported.

## Goals

- Map Kana commands and observed responses.
- Capture real Discord message/component structures before attempting automation.
- Build a transport-independent Kana adapter.
- Reuse proven automation architecture patterns: scheduling, cooldowns, state, queues, parsing, and modular actions.
- Keep secrets out of source control.
- Separate observations from assumptions.

## Project layout

```text
kana-lab/
├── docs/
├── examples/
├── kana/
│   ├── client.py
│   ├── collector.py
│   ├── discord_observer.py
│   ├── models.py
│   ├── observation_schema.py
│   └── parser.py
├── observations/
├── tests/
├── tools/
├── .env.example
├── requirements.txt
└── README.md
```

## Safety

Do not commit account tokens, cookies, passwords, or session credentials. The project is intended to use supported/authorized interfaces and normal bot interactions; it does not implement authentication bypass, CAPTCHA bypass, or stealth/evasion mechanisms. The current observer only records events; it does not automatically click components or execute commands.
