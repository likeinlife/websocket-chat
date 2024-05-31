from dataclasses import dataclass

from domain.entities._messages import (
    Chat,
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
class CreateMessageCommandHandler(BaseCommandHandler[CreateMessageCommand, Chat]):
    chats_repository: IChatRepository
    message_repository: IMessageRepository

    async def handle(self, command: CreateMessageCommand) -> Message:
        try:
            chat = await self.chats_repository.fetch_by_id(command.chat_id)
        except ChatNotFoundError:
            chat = await self.chats_repository.add(command.chat_id)

        message = Message(text=Text(value=command.message_text), chat_id=command.chat_id, user=command.user)
        chat.add_message(message)
        await self.message_repository.add(message=message)
        await self._mediator.publish(chat.pull_events())

        return message
