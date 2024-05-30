import typing as tp

from domain.events import BaseEvent
from logic.events.handlers import BaseEventHandler

from ._base import BaseEventMediator

ET = tp.TypeVar("ET", bound=BaseEvent)
ER = tp.TypeVar("ER")


class EventMediator(BaseEventMediator[ET, ER]):
    def register_event(self, event: type[ET], event_handlers: tp.Iterable[BaseEventHandler[ET, ER]]) -> None:
        self.events_map[event].extend(event_handlers)

    async def publish(self, events: tp.Iterable[ET]) -> tp.Iterable[ER]:
        result = []

        for event in events:
            handlers = self.events_map[event.__class__]
            result.extend([await handler.handle(event) for handler in handlers])

        return result
