import typing as tp
import uuid
from dataclasses import dataclass, field

from domain.events import BaseEvent

from ._base import IEventRepository


@dataclass
class InMemoryEventRepository(IEventRepository):
    _events: dict[uuid.UUID, BaseEvent] = field(default_factory=dict, kw_only=True)

    async def add(self, event: BaseEvent) -> None:
        self._events[event.event_id] = event

    async def fetch(self, event_id: uuid.UUID) -> BaseEvent | None:
        return self._events.get(event_id)

    async def fetch_list(self) -> tp.Iterable[BaseEvent]:
        return self._events.values()
