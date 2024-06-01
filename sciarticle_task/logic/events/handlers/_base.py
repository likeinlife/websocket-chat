import typing as tp

from domain.events import BaseEvent
from logic.mediator_pattern import IMediatorHandler

ET = tp.TypeVar("ET", bound=BaseEvent)
ER = tp.TypeVar("ER")


class BaseEventHandler(IMediatorHandler[ET, ER]): ...
