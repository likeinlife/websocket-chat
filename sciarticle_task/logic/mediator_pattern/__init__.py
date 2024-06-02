"""Mediator pattern interfaces."""

from ._errors import HandlerNotRegisteredError, MediatorError
from ._handler import IMediatorHandler
from ._logged_event_proxy import LoggingEventHandlerProxy
from ._mediator import BaseMediator

__all__ = (
    "IMediatorHandler",
    "BaseMediator",
    "HandlerNotRegisteredError",
    "MediatorError",
    "LoggingEventHandlerProxy",
)
