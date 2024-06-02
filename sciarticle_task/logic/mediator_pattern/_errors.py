from dataclasses import dataclass

from domain.events import BaseEvent
from logic.errors import LogicError

from ._handler import IMediatorHandler


@dataclass(frozen=True, eq=False)
class MediatorError(LogicError):
    """Base mediator error."""

    @property
    def message(self) -> str:
        return "Command mediator error"


@dataclass(frozen=True, eq=False)
class HandlerNotRegisteredError(MediatorError):
    """Mediator not registered error."""

    mediator_entity: type[BaseEvent]

    @property
    def message(self) -> str:
        return f"Command handler {self.mediator_entity} not registered"


@dataclass(frozen=True, eq=False)
class HandlerEventTypeError(MediatorError):
    """Wrong mediator entity type."""

    got_event: type[BaseEvent]
    need_event: type[BaseEvent]
    handler: IMediatorHandler

    @property
    def message(self) -> str:
        return f"Wrong command handler {self.handler} type. Need - {self.need_event}, got - {self.got_event}"


@dataclass(frozen=True, eq=False)
class InvalidEventTypeError(MediatorError):
    """Invalid mediator event type."""

    got_event: type[BaseEvent]
    need_event: type[BaseEvent]

    @property
    def message(self) -> str:
        return f"Invalid mediator event type {self.got_event} type. Need - {self.need_event}"
