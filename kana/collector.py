from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .observation_schema import new_observation, validate_observation_shape


def save_observation(path: str | Path, data: dict[str, Any]) -> Path:
    """Validate and save a credential-free observation JSON file."""
    errors = validate_observation_shape(data)
    if errors:
        raise ValueError("invalid observation: " + "; ".join(errors))

    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def collect_manual(
    observation_id: str,
    command: str,
    content: str | None,
    *,
    notes: str = "",
) -> dict[str, Any]:
    """Create an observation from text manually copied from a normal response."""
    return new_observation(
        observation_id,
        command,
        content=content,
        notes=notes,
    )
