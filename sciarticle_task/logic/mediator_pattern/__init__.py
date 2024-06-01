"""Mediator pattern interfaces."""

from ._entity import BaseMediatorEntity
from ._errors import CommandHandlerNotRegisteredError, CommandMediatorError
from ._handler import IMediatorHandler
from ._mediator import BaseMediator

__all__ = (
    "BaseMediatorEntity",
    "IMediatorHandler",
    "BaseMediator",
    "CommandHandlerNotRegisteredError",
    "CommandMediatorError",
)
