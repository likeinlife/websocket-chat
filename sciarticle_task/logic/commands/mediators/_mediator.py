import typing as tp

from logic.commands.entities import BaseCommand
from logic.commands.handlers import BaseCommandHandler

from ._base import BaseCommandMediator
from .errors import CommandHandlerNotRegisteredError

CT = tp.TypeVar("CT", bound=BaseCommand)
CR = tp.TypeVar("CR")


class CommandMediator(BaseCommandMediator[CT, CR]):
    def register_command(self, command: type[CT], command_handlers: tp.Iterable[BaseCommandHandler[CT, CR]]) -> None:
        self.commands_map[command].extend(command_handlers)

    async def handle_command(self, command: CT) -> tp.Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlerNotRegisteredError(command_type)

        return [await handler.handle(command) for handler in handlers]
