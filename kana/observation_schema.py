from __future__ import annotations

from datetime import datetime
from typing import Any

SCHEMA_VERSION = 1


def validate_observation_shape(data: Any) -> list[str]:
    """Validate the portable observation format without requiring jsonschema."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["observation must be a JSON object"]

    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")

    for key in ("id", "command", "observed_at", "response"):
        if key not in data:
            errors.append(f"missing required field: {key}")

    if "id" in data and not isinstance(data["id"], str):
        errors.append("id must be a string")
    if "command" in data and not isinstance(data["command"], str):
        errors.append("command must be a string")
    if "observed_at" in data:
        if not isinstance(data["observed_at"], str):
            errors.append("observed_at must be an ISO-8601 string")
        else:
            try:
                datetime.fromisoformat(data["observed_at"].replace("Z", "+00:00"))
            except ValueError:
                errors.append("observed_at must be a valid ISO-8601 timestamp")

    response = data.get("response")
    if "response" in data and not isinstance(response, dict):
        errors.append("response must be an object")
    elif isinstance(response, dict):
        if "type" in response and not isinstance(response["type"], str):
            errors.append("response.type must be a string")
        if "content" in response and response["content"] is not None and not isinstance(response["content"], str):
            errors.append("response.content must be a string or null")
        if "embeds" in response and not isinstance(response["embeds"], list):
            errors.append("response.embeds must be an array")
        if "components" in response and not isinstance(response["components"], list):
            errors.append("response.components must be an array")

    if "notes" in data and not isinstance(data["notes"], str):
        errors.append("notes must be a string")
    return errors


def new_observation(
    observation_id: str,
    command: str,
    *,
    response_type: str = "message",
    content: str | None = None,
    embeds: list[dict[str, Any]] | None = None,
    components: list[dict[str, Any]] | None = None,
    notes: str = "",
) -> dict[str, Any]:
    """Create a clean observation skeleton for manual or programmatic collection."""
    return {
        "schema_version": SCHEMA_VERSION,
        "id": observation_id,
        "command": command,
        "observed_at": datetime.now().astimezone().isoformat(),
        "response": {
            "type": response_type,
            "content": content,
            "embeds": embeds or [],
            "components": components or [],
        },
        "notes": notes,
    }
