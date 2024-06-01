"""Mediator pattern interfaces."""

from ._errors import HandlerNotRegisteredError, MediatorError
from ._handler import IMediatorHandler
from ._mediator import BaseMediator

__all__ = (
    "IMediatorHandler",
    "BaseMediator",
    "HandlerNotRegisteredError",
    "MediatorError",
)
