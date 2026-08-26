from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import discord
from dotenv import load_dotenv

load_dotenv()


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def embed_to_dict(embed: discord.Embed) -> dict[str, Any]:
    return embed.to_dict()


def component_to_dict(component: Any) -> dict[str, Any]:
    data: dict[str, Any] = {"type": getattr(component, "type", None).__str__()}
    for key in ("custom_id", "label", "style", "url", "disabled", "placeholder", "min_values", "max_values"):
        value = getattr(component, key, None)
        if value is not None:
            data[key] = value.name if hasattr(value, "name") else value
    if hasattr(component, "options"):
        data["options"] = [
            {
                key: (getattr(option, key, None).name if hasattr(getattr(option, key, None), "name") else getattr(option, key, None))
                for key in ("label", "value", "description", "default", "emoji")
                if getattr(option, key, None) is not None
            }
            for option in component.options
        ]
    return data


def message_to_record(message: discord.Message, event: str) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "event": event,
        "observed_at": iso_now(),
        "message": {
            "id": str(message.id),
            "channel_id": str(message.channel.id),
            "guild_id": str(message.guild.id) if message.guild else None,
            "author": {
                "id": str(message.author.id),
                "name": str(message.author),
                "bot": message.author.bot,
            },
            "content": message.content,
            "created_at": message.created_at.isoformat(),
            "edited_at": message.edited_at.isoformat() if message.edited_at else None,
            "embeds": [embed_to_dict(embed) for embed in message.embeds],
            "components": [component_to_dict(c) for c in message.components],
            "attachments": [
                {"id": str(a.id), "filename": a.filename, "content_type": a.content_type, "size": a.size}
                for a in message.attachments
            ],
            "reference": {
                "message_id": str(message.reference.message_id) if message.reference and message.reference.message_id else None,
                "channel_id": str(message.reference.channel_id) if message.reference and message.reference.channel_id else None,
                "guild_id": str(message.reference.guild_id) if message.reference and message.reference.guild_id else None,
            },
        },
    }


class JsonlStore:
    def __init__(self, directory: str | Path) -> None:
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / "events.jsonl"

    def append(self, record: dict[str, Any]) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


class KanaObserver(discord.Client):
    def __init__(self, channel_id: int, store: JsonlStore) -> None:
        intents = discord.Intents.default()
        intents.guilds = True
        intents.messages = True
        intents.message_content = True
        super().__init__(intents=intents)
        self.channel_id = channel_id
        self.store = store

    async def on_ready(self) -> None:
        channel = self.get_channel(self.channel_id)
        print(f"Connected as {self.user} ({self.user.id})")
        if channel is None:
            print(f"WARNING: channel {self.channel_id} is not visible to this bot.")
        else:
            print(f"Observing #{getattr(channel, 'name', channel.id)} ({self.channel_id})")

    def _matches(self, message: discord.Message) -> bool:
        return message.channel.id == self.channel_id

    async def on_message(self, message: discord.Message) -> None:
        if self._matches(message):
            self.store.append(message_to_record(message, "message_create"))
            print(f"[CREATE] {message.id} {message.author}: {message.content[:80]!r}")

    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        if self._matches(after):
            record = message_to_record(after, "message_edit")
            record["before"] = {"content": before.content, "embeds": [embed_to_dict(e) for e in before.embeds]}
            self.store.append(record)
            print(f"[EDIT] {after.id}")

    async def on_message_delete(self, message: discord.Message) -> None:
        if self._matches(message):
            self.store.append(message_to_record(message, "message_delete"))
            print(f"[DELETE] {message.id}")


def main() -> None:
    token = os.getenv("DISCORD_BOT_TOKEN", "").strip()
    channel_raw = os.getenv("OBSERVE_CHANNEL_ID", "").strip()
    data_dir = os.getenv("DATA_DIR", "./observations/runtime").strip()

    if not token:
        raise SystemExit("DISCORD_BOT_TOKEN is required. Use a Discord bot token, never a user token.")
    if not channel_raw.isdigit():
        raise SystemExit("OBSERVE_CHANNEL_ID must be a numeric Discord channel ID.")

    client = KanaObserver(int(channel_raw), JsonlStore(data_dir))
    client.run(token)


if __name__ == "__main__":
    main()
