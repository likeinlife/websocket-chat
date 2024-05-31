import typing as tp
from dataclasses import dataclass

from logic.commands.entities import BaseCommand
from logic.errors import LogicError


class CommandMediatorError(LogicError):
    """Base command mediator error."""

    @property
    def message(self) -> str:
        return "Command mediator error"


@dataclass
class CommandHandlerNotRegisteredError(CommandMediatorError):
    """Command mediator not registered error."""

    command: type[BaseCommand]

    @property
    def message(self) -> str:
        return f"Command handler {self.command} not registered"


@dataclass
class WrongCommandHandlerTypeError(CommandMediatorError):
    """Command mediator not registered error."""

    command: tp.Any
    need_type: type[BaseCommand]
    handler: tp.Any

    @property
    def message(self) -> str:
        return f"Wrong command handler {self.handler} type. Need - {self.need_type}, got - {self.command}"
