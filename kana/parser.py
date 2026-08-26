from typing import Any

from .models import Observation


def observation_from_message(
    action: str,
    content: str | None,
    *,
    response_type: str = "message",
    metadata: dict[str, Any] | None = None,
) -> Observation:
    """Normalize an observed response without assuming Kana's private protocol."""

    return Observation(
        action=action,
        response_type=response_type,
        content=content,
        metadata=metadata or {},
    )
