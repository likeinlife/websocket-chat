import asyncio

from domain.entities import Message
from logic.commands.entities import BaseCommand
from logic.mediator_pattern import BaseMediator


class CommandMediator(BaseMediator[Message, Message]):
    """Mediator for commands.

    Command should be created by user.
    """

    _allow_event_type = BaseCommand

    async def handle(self, entity: BaseCommand) -> Message:
        handlers = self._get_handlers(entity)

        done = await asyncio.gather(*[handler.handle(entity) for handler in handlers])
        return done[0]
