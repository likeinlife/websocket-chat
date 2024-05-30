import abc
import typing as tp
from dataclasses import dataclass, field

from logic.queries.entities import BaseQuery
from logic.queries.handlers import BaseQueryHandler

QT = tp.TypeVar("QT", bound=BaseQuery)
QR = tp.TypeVar("QR")


@dataclass
class BaseQueryMediator(abc.ABC, tp.Generic[QT, QR]):
    queries_map: dict[type[QT], BaseQueryHandler] = field(
        default_factory=dict,
        kw_only=True,
    )

    @abc.abstractmethod
    def register_query(self, query: type[QT], query_handler: BaseQueryHandler[QT, QR]) -> None: ...

    @abc.abstractmethod
    async def handle_query(self, query: BaseQuery) -> QR: ...
