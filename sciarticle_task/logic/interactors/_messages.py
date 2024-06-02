from dataclasses import dataclass

from domain.entities import Message
from infra.repositories.messages import IMessageRepository
from logic.usecases import FetchChatMessagesUseCase, FetchMessageUseCase


@dataclass(slots=True)
class MessageInteractor:
    message_repo: IMessageRepository

    async def fetch_chat_messages(self, chat_id: str) -> list[Message]:
        return await FetchChatMessagesUseCase(message_repo=self.message_repo, chat_id=chat_id)()

    async def fetch_message(self, message_id: str) -> Message | None:
        return await FetchMessageUseCase(message_repo=self.message_repo, message_id=message_id)()
