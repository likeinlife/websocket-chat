from collections import defaultdict
from dataclasses import dataclass, field

from domain.entities import Message
from infra.repositories.errors import ChatNotFoundError, MessageNotFoundError

from ._base import IMessageRepository


@dataclass
class InMemoryMessageRepository(IMessageRepository):
    messages: dict[str, list[Message]] = field(default_factory=lambda: defaultdict(list), kw_only=True)
    message_ids: dict[str, Message] = field(default_factory=dict, kw_only=True)

    async def fetch_from_chat(self, chat_id: str) -> list[Message]:
        if chat_id not in self.messages:
            raise ChatNotFoundError(chat_id=chat_id)
        return self.messages.get(chat_id, [])

    async def add(self, message: Message) -> None:
        self.messages[message.chat_id].append(message)
        self.message_ids[message.id] = message

    async def fetch(self, message_id: str) -> Message:
        result = self.message_ids.get(message_id)
        if not result:
            raise MessageNotFoundError(message_id=message_id)
        return result
