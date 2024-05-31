from dataclasses import dataclass

import structlog
from domain.entities._messages import Message
from infra.repositories.messages import IMessageRepository
from logic.queries.entities import FetchMessagesQuery

from ._base import BaseQueryHandler


@dataclass
class FetchMessagesQueryHandler(BaseQueryHandler[FetchMessagesQuery, list[Message]]):
    message_repository: IMessageRepository
    _logger = structlog.getLogger()

    async def handle(self, query: FetchMessagesQuery) -> list[Message]:
        self._logger.debug("Handle fetch_messages_query", chat_id=query.chat_id)
        return await self.message_repository.fetch(query.chat_id)
