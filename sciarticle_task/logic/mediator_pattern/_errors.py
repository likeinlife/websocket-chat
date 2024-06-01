from dataclasses import dataclass

from logic.errors import LogicError

from ._entity import BaseMediatorEntity
from ._handler import IMediatorHandler


class MediatorError(LogicError):
    """Base mediator error."""

    @property
    def message(self) -> str:
        return "Command mediator error"


@dataclass
class HandlerNotRegisteredError(MediatorError):
    """Mediator not registered error."""

    mediator_entity: type[BaseMediatorEntity]

    @property
    def message(self) -> str:
        return f"Command handler {self.mediator_entity} not registered"


@dataclass
class HandlerEntityTypeError(MediatorError):
    """Wrong mediator entity type."""

    got_mediator_entity: type[BaseMediatorEntity]
    need_entity: type[BaseMediatorEntity]
    handler: IMediatorHandler

    @property
    def message(self) -> str:
        return f"Wrong command handler {self.handler} type. Need - {self.need_entity}, got - {self.got_mediator_entity}"
