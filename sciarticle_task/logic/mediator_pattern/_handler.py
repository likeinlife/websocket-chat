import abc
import typing as tp

from domain.events import BaseEvent

EVENT = tp.TypeVar("EVENT", bound=BaseEvent)
HANDLER_RETURN = tp.TypeVar("HANDLER_RETURN")


class IMediatorHandler(abc.ABC, tp.Generic[EVENT, HANDLER_RETURN]):
    @abc.abstractmethod
    async def handle(self, event: EVENT) -> HANDLER_RETURN: ...
