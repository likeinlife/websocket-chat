import abc
import typing as tp
from dataclasses import dataclass

from domain.events import BaseEvent
from infra.websockets import BaseWebSocketConnectionManager

ET = tp.TypeVar("ET", bound=BaseEvent)
ER = tp.TypeVar("ER")


@dataclass
class BaseEventHandler(abc.ABC, tp.Generic[ET, ER]):
    connection_manager: BaseWebSocketConnectionManager

    @abc.abstractmethod
    async def handle(self, event: ET) -> ER: ...
