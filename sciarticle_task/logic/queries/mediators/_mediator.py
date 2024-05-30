import typing as tp

from logic.queries.entities import BaseQuery
from logic.queries.handlers import BaseQueryHandler

from ._base import BaseQueryMediator

QT = tp.TypeVar("QT", bound=BaseQuery)
QR = tp.TypeVar("QR")


class QueryMediator(BaseQueryMediator[QT, QR]):
    def register_query(self, query: type[QT], query_handler: BaseQueryHandler[QT, QR]) -> None:
        self.queries_map[query] = query_handler

    async def handle_query(self, query: QT) -> QR:
        return await self.queries_map[query.__class__].handle(query=query)
