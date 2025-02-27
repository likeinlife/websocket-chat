"""Use cases."""

from ._chats import FetchChatMessagesUseCase
from ._errors import ChatNotFoundError, UseCaseError
from ._events import FetchEventByID, FetchEventList
from ._interface import IUseCase
from ._messages import FetchMessageUseCase

__all__ = (
    "FetchMessageUseCase",
    "ChatNotFoundError",
    "UseCaseError",
    "IUseCase",
    "FetchChatMessagesUseCase",
    "FetchEventList",
    "FetchEventByID",
)
