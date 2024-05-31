import asyncio
import typing as tp

from logic.commands.entities import BaseCommand
from logic.commands.handlers import BaseCommandHandler

from ._base import BaseCommandMediator
from ._response import MediatorResponse
from .errors import CommandHandlerNotRegisteredError, WrongCommandHandlerTypeError

CR = tp.TypeVar("CR")


class CommandMediator(BaseCommandMediator[CR]):
    def register_command(
        self,
        command: type[BaseCommand],
        command_handlers: tp.Iterable[BaseCommandHandler[CR]],
    ) -> None:
        for handler in command_handlers:
            try:
                command_handler_type = tp.get_type_hints(handler.handle)["command"]
            except (KeyError, AttributeError) as e:
                raise WrongCommandHandlerTypeError(None, command, handler) from e

            if command_handler_type != command:
                raise WrongCommandHandlerTypeError(command, command_handler_type, handler)

            self.commands_map[command].append(handler)

    async def handle_command(self, command: BaseCommand) -> MediatorResponse:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlerNotRegisteredError(command_type)

        done = await asyncio.gather(*[handler.handle(command) for handler in handlers])
        return MediatorResponse(command.id, done)
