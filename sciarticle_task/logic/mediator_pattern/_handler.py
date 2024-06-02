import abc
import typing as tp
from dataclasses import dataclass

from domain.events import BaseEvent

EVENT = tp.TypeVar("EVENT", bound=BaseEvent)
HANDLER_RETURN = tp.TypeVar("HANDLER_RETURN")


@dataclass
class IMediatorHandler(abc.ABC, tp.Generic[EVENT, HANDLER_RETURN]):
    event_type: type[EVENT]

    @abc.abstractmethod
    async def handle(self, event: EVENT) -> HANDLER_RETURN: ...
