import abc
import typing as tp
from collections import defaultdict
from dataclasses import dataclass, field

from domain.events import BaseEvent
from logic.events.handlers import BaseEventHandler

ET = tp.TypeVar("ET", bound=BaseEvent)
ER = tp.TypeVar("ER")
S = tp.TypeVar("S", bound=BaseEvent)


@dataclass
class BaseEventMediator(abc.ABC, tp.Generic[ET, ER]):
    events_map: dict[type[ET], list[BaseEventHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    @abc.abstractmethod
    def register_event(self, event: type[ET], event_handlers: tp.Iterable[BaseEventHandler[ET, ER, S]]) -> None: ...

    @abc.abstractmethod
    async def publish(self, events: tp.Iterable[BaseEvent]) -> tp.Iterable[ER]: ...
