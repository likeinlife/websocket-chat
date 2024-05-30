import abc

from domain.entities import Chat


class IChatRepository(abc.ABC):
    @abc.abstractmethod
    async def fetch_by_id(self, chat_id: str) -> Chat:
        """Fetch chat."""

    @abc.abstractmethod
    async def add(self) -> Chat:
        """Add new chat."""

    @abc.abstractmethod
    async def delete(self, chat_id: str) -> None:
        """Delete chat."""
