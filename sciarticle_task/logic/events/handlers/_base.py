import abc
import typing as tp
from dataclasses import dataclass

from domain.events import BaseEvent
from logic.serializer import BaseEventSerializer

ET = tp.TypeVar("ET", bound=BaseEvent)
ER = tp.TypeVar("ER")
S = tp.TypeVar("S", bound=BaseEvent)


@dataclass
class BaseEventHandler(abc.ABC, tp.Generic[ET, ER, S]):
    serializer: BaseEventSerializer[S]

    @abc.abstractmethod
    async def handle(self, event: ET) -> ER: ...
