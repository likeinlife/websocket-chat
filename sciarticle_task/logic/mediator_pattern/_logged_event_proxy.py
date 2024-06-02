import typing as tp
from dataclasses import dataclass

from ._handler import IMediatorHandler
from domain.events import BaseEvent
from infra.repositories.events import IEventRepository

EVENT = tp.TypeVar("EVENT", bound=BaseEvent)
HANDLER_RETURN = tp.TypeVar("HANDLER_RETURN")


@dataclass
class LoggingEventHandlerProxy(IMediatorHandler[EVENT, HANDLER_RETURN]):
    handler: IMediatorHandler[EVENT, HANDLER_RETURN]
    event_repo: IEventRepository

    async def handle(self, event: EVENT) -> HANDLER_RETURN:
        await self.event_repo.add(event)
        return await self.handler.handle(event)
