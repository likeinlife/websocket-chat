from copy import copy
from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from uuid import uuid4

from domain.events import BaseEvent


@dataclass(eq=False)
class BaseEntity:
    """Base entity class."""

    id: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    _events: list[BaseEvent] = field(default_factory=list, kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)

    def __hash__(self) -> int:
        """Entity hash base on id."""
        return hash(self.id)

    def __eq__(self, __value: "BaseEntity") -> bool:  # type: ignore
        """Compare entity id."""
        return self.id == __value.id

    def register_event(self, event: BaseEvent) -> None:
        """Register new events."""
        self._events.append(event)

    def pull_events(self) -> list[BaseEvent]:
        """Pull registered events."""
        registered_events = copy(self._events)
        self._events.clear()

        return registered_events
