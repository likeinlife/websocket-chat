"""Messages repositories."""

from ._base import IMessageRepository
from ._in_memory import InMemoryMessageRepository

__all__ = ("IMessageRepository", "InMemoryMessageRepository")
