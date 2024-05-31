import abc
import typing as tp

from domain.events import BaseEvent

T = tp.TypeVar("T", bound=BaseEvent)


class BaseEventSerializer(abc.ABC, tp.Generic[T]):
    @abc.abstractmethod
    def serialize(self, event: T) -> dict: ...

    @abc.abstractmethod
    def deserialize(self, data: dict) -> T: ...
