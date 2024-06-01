from dataclasses import dataclass

from domain.entities import Message
from infra.repositories.chats import IChatRepository
from infra.repositories.errors import ChatNotFoundError, MessageNotFoundError
from infra.repositories.messages import IMessageRepository

from ._errors import ChatNotFoundError as LogicChatNotFoundError


@dataclass
class MessageUseCases:
    message_repo: IMessageRepository
    chat_repo: IChatRepository

    async def fetch_chat_messages(self, chat_id: str) -> list[Message]:
        try:
            return await self.message_repo.fetch_from_chat(chat_id=chat_id)
        except ChatNotFoundError as e:
            raise LogicChatNotFoundError(chat_id=chat_id) from e

    async def fetch_message(self, message_id: str) -> Message | None:
        try:
            return await self.message_repo.fetch(message_id=message_id)
        except MessageNotFoundError:
            return None
