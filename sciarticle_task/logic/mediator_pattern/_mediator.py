import abc
import typing as tp
from collections import defaultdict
from dataclasses import dataclass, field

from ._entity import BaseMediatorEntity
from ._errors import WrongEntityHandlerTypeError
from ._handler import IMediatorHandler

ENTITY = tp.TypeVar("ENTITY", bound=BaseMediatorEntity)
HANDLER_RETURN = tp.TypeVar("HANDLER_RETURN")
MEDIATOR_RETURN = tp.TypeVar("MEDIATOR_RETURN")


@dataclass
class BaseMediator(tp.Generic[ENTITY, HANDLER_RETURN, MEDIATOR_RETURN]):
    handler_map: dict[type[ENTITY], list[IMediatorHandler[ENTITY, HANDLER_RETURN]]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    def register(self, entity: type[ENTITY], handler: IMediatorHandler[ENTITY, HANDLER_RETURN]) -> None:
        """Register handler for entity.

        Note: must be at least one handler for each mediator entity.
        """
        command_handler_type = tp.get_type_hints(handler.handle)["command"]

        if command_handler_type != entity:
            raise WrongEntityHandlerTypeError(entity, command_handler_type, handler)

        self.handler_map[entity].append(handler)

    @abc.abstractmethod
    async def handle(self, entity: BaseMediatorEntity) -> MEDIATOR_RETURN: ...
