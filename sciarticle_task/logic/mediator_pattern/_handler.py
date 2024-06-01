import abc
import typing as tp

from ._entity import BaseMediatorEntity

ENTITY = tp.TypeVar("ENTITY", bound=BaseMediatorEntity)
HANDLER_RETURN = tp.TypeVar("HANDLER_RETURN")


class IMediatorHandler(abc.ABC, tp.Generic[ENTITY, HANDLER_RETURN]):
    @abc.abstractmethod
    async def handle(self, entity: ENTITY) -> HANDLER_RETURN: ...
