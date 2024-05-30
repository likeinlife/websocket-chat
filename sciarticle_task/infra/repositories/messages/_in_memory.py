from collections import defaultdict
from dataclasses import dataclass, field

from domain.entities import Message

from ._base import IMessageRepository


@dataclass
class InMemoryMessageRepository(IMessageRepository):
    messages: dict[str, list[Message]] = field(default_factory=lambda: defaultdict(list), kw_only=True)

    async def fetch(self, chat_id: str) -> list[Message]:
        return self.messages.get(chat_id, [])

    async def add(self, message: Message) -> None:
        self.messages[message.chat_id].append(message)
