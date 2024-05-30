import abc
import typing as tp

from logic.queries.entities import BaseQuery

QT = tp.TypeVar("QT", bound=BaseQuery)
QR = tp.TypeVar("QR")


class BaseQueryHandler(abc.ABC, tp.Generic[QT, QR]):
    @abc.abstractmethod
    async def handle(self, query: QT) -> QR: ...
