"""Core module for settings and logging."""

from ._logging import configure_logging
from ._settings import settings

__all__ = ("settings", "configure_logging")
