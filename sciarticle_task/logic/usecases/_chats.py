from dataclasses import dataclass

from domain.entities import Message
from infra.repositories.errors import ChatNotFoundError
from infra.repositories.messages import IMessageRepository

from ._errors import ChatNotFoundError as LogicChatNotFoundError
from ._interface import IUseCase


@dataclass
class FetchChatMessagesUseCase(IUseCase[list[Message]]):
    message_repo: IMessageRepository
    chat_id: str

    async def __call__(self) -> list[Message]:
        try:
            return await self.message_repo.fetch_from_chat(chat_id=self.chat_id)
        except ChatNotFoundError as e:
            raise LogicChatNotFoundError(chat_id=self.chat_id) from e
