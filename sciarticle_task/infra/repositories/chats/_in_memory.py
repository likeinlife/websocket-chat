from dataclasses import dataclass, field

from domain.entities import Chat
from infra.repositories.errors import ChatNotFoundError

from ._base import IChatRepository


@dataclass
class InMemoryChatRepository(IChatRepository):
    chats: dict[str, Chat] = field(default_factory=dict, kw_only=True)

    async def fetch_by_id(self, chat_id: str) -> Chat:
        chat = self.chats.get(chat_id)
        if not chat:
            raise ChatNotFoundError(chat_id=chat_id)
        return chat

    async def add(self) -> Chat:
        chat = Chat()
        self.chats[chat.id] = chat
        return chat

    async def delete(self, chat_id: str) -> None:
        if not self.chats.get(chat_id):
            raise ChatNotFoundError(chat_id=chat_id)
        del self.chats[chat_id]
