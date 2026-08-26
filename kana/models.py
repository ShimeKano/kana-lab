from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Observation:
    """Non-sensitive observation captured during an authorized experiment."""

    action: str
    response_type: str | None = None
    content: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    observed_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class Cooldown:
    command: str
    ready_at: datetime

    def remaining_seconds(self, now: datetime | None = None) -> float:
        now = now or datetime.utcnow()
        return max(0.0, (self.ready_at - now).total_seconds())
