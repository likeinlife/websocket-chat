"""DI container."""

from core import configure_logging, settings
from dependency_injector import providers as p
from dependency_injector.containers import DeclarativeContainer


class LoggingContainer(DeclarativeContainer):
    """Main DI container."""

    logger: p.Resource = p.Resource(
        configure_logging,
        level=settings.logging.level,
        json_format=settings.logging.json_format,
    )


class Container(DeclarativeContainer):
    """Main DI container."""

    _log = p.Container(LoggingContainer)
