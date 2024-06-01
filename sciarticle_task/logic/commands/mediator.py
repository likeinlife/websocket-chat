import asyncio

from domain.entities import Message
from logic.commands.entities import BaseCommand
from logic.mediator_pattern import BaseMediator


class CommandMediator(BaseMediator[BaseCommand, Message, Message]):
    """Mediator for commands."""

    async def handle(self, entity: BaseCommand) -> Message:
        handlers = self._get_handler(entity)

        done = await asyncio.gather(*[handler.handle(entity) for handler in handlers])
        return done[0]
