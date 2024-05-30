import abc

from domain.entities import Message


class IMessageRepository(abc.ABC):
    @abc.abstractmethod
    async def fetch(self, chat_id: str) -> list[Message]:
        """Fetch chat messages."""

    @abc.abstractmethod
    async def add(self, message: Message) -> None:
        """Add new message."""
