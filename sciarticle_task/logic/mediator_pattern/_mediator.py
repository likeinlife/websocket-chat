import abc
import typing as tp
from collections import defaultdict
from dataclasses import dataclass, field

from domain.events import BaseEvent

from ._errors import HandlerEventTypeError, HandlerNotRegisteredError, InvalidEventTypeError
from ._handler import IMediatorHandler

EVENT = tp.TypeVar("EVENT", bound=BaseEvent)
HANDLER_RETURN = tp.TypeVar("HANDLER_RETURN")
MEDIATOR_RETURN = tp.TypeVar("MEDIATOR_RETURN")


@dataclass
class BaseMediator(tp.Generic[HANDLER_RETURN, MEDIATOR_RETURN]):
    _allow_event_type: tp.ClassVar
    handler_map: dict[type[BaseEvent], list[IMediatorHandler[BaseEvent, HANDLER_RETURN]]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    def register(self, event: type[EVENT], handler: IMediatorHandler[EVENT, HANDLER_RETURN]) -> None:
        """Register handler for event.

        Note: must be at least one handler for each mediator entity.
        """
        if not isinstance(event, self._allow_event_type):
            raise InvalidEventTypeError(event, self._allow_event_type)
        command_handler_type = tp.get_type_hints(handler.handle)["command"]

        if command_handler_type != event:
            raise HandlerEventTypeError(event, command_handler_type, handler)

        self.handler_map[event].append(handler)  # type: ignore

    @abc.abstractmethod
    async def handle(self, event: BaseEvent) -> MEDIATOR_RETURN: ...

    def _get_handlers(self, event: EVENT) -> list[IMediatorHandler[EVENT, HANDLER_RETURN]]:
        """Get registered handler for entity.

        Raises
        ------
        HandlerNotRegisteredError if not found.

        """
        entity_type = type(event)
        handlers = self.handler_map.get(entity_type)
        if not handlers:
            raise HandlerNotRegisteredError(entity_type)
        return handlers  # type: ignore
