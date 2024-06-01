from dataclasses import dataclass

from logic.errors import LogicError

from ._entity import BaseMediatorEntity
from ._handler import IMediatorHandler


class CommandMediatorError(LogicError):
    """Base command mediator error."""

    @property
    def message(self) -> str:
        return "Command mediator error"


@dataclass
class CommandHandlerNotRegisteredError(CommandMediatorError):
    """Command mediator not registered error."""

    mediator_entity: type[BaseMediatorEntity]

    @property
    def message(self) -> str:
        return f"Command handler {self.mediator_entity} not registered"


@dataclass
class WrongEntityHandlerTypeError(CommandMediatorError):
    """Command mediator not registered error."""

    got_mediator_entity: type[BaseMediatorEntity]
    need_entity: type[BaseMediatorEntity]
    handler: IMediatorHandler

    @property
    def message(self) -> str:
        return f"Wrong command handler {self.handler} type. Need - {self.need_entity}, got - {self.got_mediator_entity}"
