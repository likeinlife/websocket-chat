from dataclasses import dataclass

import structlog
from domain.entities._messages import (
    Message,
)
from domain.values import (
    Text,
)
from infra.repositories.chats import IChatRepository
from infra.repositories.errors import ChatNotFoundError
from infra.repositories.messages import IMessageRepository
from logic.commands.entities import CreateMessageCommand

from ._base import BaseCommandHandler


@dataclass
class CreateMessageCommandHandler(BaseCommandHandler[CreateMessageCommand, Message]):
    chats_repository: IChatRepository
    message_repository: IMessageRepository
    _logger = structlog.getLogger()

    async def handle(self, event: CreateMessageCommand) -> Message:
        try:
            chat = await self.chats_repository.fetch_by_id(event.chat_id)
        except ChatNotFoundError:
            chat = await self.chats_repository.add(event.chat_id)

        message = Message(text=Text(value=event.message_text), chat_id=event.chat_id, user=event.user)
        self._logger.debug("Handle create_message_command", chat_id=event.chat_id, user=event.user)
        chat.add_message(message)
        await self.message_repository.add(message=message)
        [await self.event_mediator.handle(event) for event in chat.pull_events()]

        return message
