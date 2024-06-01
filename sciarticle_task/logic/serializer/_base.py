import abc
import typing as tp

from domain.events import BaseEvent

T = tp.TypeVar("T", bound=BaseEvent)


class BaseEventSerializer(abc.ABC):
    @abc.abstractmethod
    def serialize(self, event: BaseEvent) -> dict: ...

    @abc.abstractmethod
    def deserialize(self, data: dict, event_type: type[T]) -> T: ...
