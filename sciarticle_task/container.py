"""DI container."""

from core import configure_logging, settings
from dependency_injector import providers as p
from dependency_injector.containers import DeclarativeContainer
from infra.repositories.chats import InMemoryChatRepository
from infra.repositories.messages import InMemoryMessageRepository
from infra.websockets import WebSocketConnectionManager
from logic import init
from logic.mediator import Mediator


class LogicContainer(DeclarativeContainer):
    """Logic container."""

    websockets_manager: p.Singleton = p.Singleton(WebSocketConnectionManager)
    chat_repository: p.Singleton = p.Singleton(InMemoryChatRepository)
    message_repository: p.Singleton = p.Singleton(InMemoryMessageRepository)
    event_mediator: p.Singleton = p.Singleton(
        init.init_event_mediator,
        websockets_manager,
    )
    command_mediator: p.Singleton = p.Singleton(
        init.init_command_mediator,
        event_mediator,
        chat_repository,
        message_repository,
    )
    query_mediator: p.Singleton = p.Singleton(
        init.init_query_mediator,
        message_repository,
    )

    mediator: p.Singleton = p.Singleton(
        Mediator,
        query_mediator=query_mediator,
        event_mediator=event_mediator,
        command_mediator=command_mediator,
    )


class LoggingContainer(DeclarativeContainer):
    """Logging container."""

    logger: p.Resource = p.Resource(
        configure_logging,
        level=settings.logging.level,
        json_format=settings.logging.json_format,
    )


class Container(DeclarativeContainer):
    """Main DI container."""

    _log = p.Container(LoggingContainer)
    logic = p.Container(LogicContainer)
