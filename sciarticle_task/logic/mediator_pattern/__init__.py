"""Mediator pattern interfaces."""

from ._entity import BaseMediatorEntity
from ._errors import HandlerNotRegisteredError, MediatorError
from ._handler import IMediatorHandler
from ._mediator import BaseMediator

__all__ = (
    "BaseMediatorEntity",
    "IMediatorHandler",
    "BaseMediator",
    "HandlerNotRegisteredError",
    "MediatorError",
)
