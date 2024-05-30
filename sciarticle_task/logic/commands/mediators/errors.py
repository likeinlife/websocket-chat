from dataclasses import dataclass

from domain.errors import BaseError
from logic.commands.entities import BaseCommand


class CommandMediatorError(BaseError):
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
        return "Command handler not registered"
