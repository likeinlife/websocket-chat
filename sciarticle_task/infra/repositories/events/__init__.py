"""Event repositories."""

from ._base import IEventRepository
from ._in_memory import InMemoryEventRepository

__all__ = ("IEventRepository", "InMemoryEventRepository")
