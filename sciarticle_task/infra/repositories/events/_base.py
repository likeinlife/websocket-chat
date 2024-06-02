import abc
import typing as tp
import uuid

from domain.events import BaseEvent


class IEventRepository(abc.ABC):
    @abc.abstractmethod
    async def fetch(self, event_id: uuid.UUID) -> BaseEvent | None:
        """Fetch event by id."""

    @abc.abstractmethod
    async def add(self, event: BaseEvent) -> None:
        """Log new event."""

    @abc.abstractmethod
    async def fetch_list(self) -> tp.Iterable[BaseEvent]:
        """Fetch all events."""
