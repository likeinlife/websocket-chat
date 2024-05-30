"""Chats repositories."""

from ._base import IChatRepository
from ._in_memory import InMemoryChatRepository

__all__ = ("IChatRepository", "InMemoryChatRepository")
