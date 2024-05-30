from dataclasses import dataclass

from domain.entities._messages import Message
from infra.repositories.messages import IMessageRepository
from logic.queries.entities import FetchMessagesQuery

from ._base import BaseQueryHandler


@dataclass
class FetchMessagesQueryHandler(BaseQueryHandler[FetchMessagesQuery, list[Message]]):
    message_repository: IMessageRepository

    async def handle(self, query: FetchMessagesQuery) -> list[Message]:
        return await self.message_repository.fetch(query.chat_id)
