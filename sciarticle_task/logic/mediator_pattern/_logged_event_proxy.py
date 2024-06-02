import typing as tp
from dataclasses import dataclass, field

from domain.events import BaseEvent
from infra.repositories.events import IEventRepository

from ._handler import IMediatorHandler

EVENT = tp.TypeVar("EVENT", bound=BaseEvent)
HANDLER_RETURN = tp.TypeVar("HANDLER_RETURN")


@dataclass
class LoggingEventHandlerProxy(IMediatorHandler[EVENT, HANDLER_RETURN]):
    handler: IMediatorHandler[EVENT, HANDLER_RETURN]
    event_repo: IEventRepository
    event_type: EVENT = field(init=False)

    def __post_init__(self) -> None:
        """Inherit event type from handler."""
        self.event_type = self.handler.event_type  # type: ignore

    async def handle(self, event: EVENT) -> HANDLER_RETURN:
        await self.event_repo.add(event)
        return await self.handler.handle(event)
