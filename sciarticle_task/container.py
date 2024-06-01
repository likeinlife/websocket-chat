"""DI container."""

import aiojobs
from core import configure_logging, settings
from dependency_injector import providers as p
from dependency_injector.containers import DeclarativeContainer
from infra.brokers import init_rabbitmq_broker
from infra.repositories.chats import InMemoryChatRepository
from infra.repositories.messages import InMemoryMessageRepository
from infra.websockets import WebSocketConnectionManager
from logic import init
from logic.mediator import Mediator
from logic.serializer import EventSerializer
from logic.usecases import MessageUseCases


class InfraContainer(DeclarativeContainer):
    """Brokers container."""

    scheduler: p.Factory = p.Factory(aiojobs.Scheduler)
    broker: p.Singleton = p.Singleton(init_rabbitmq_broker, settings.rabbit.url)
    websockets_manager: p.Singleton = p.Singleton(WebSocketConnectionManager)
    chat_repository: p.Singleton = p.Singleton(InMemoryChatRepository)
    message_repository: p.Singleton = p.Singleton(InMemoryMessageRepository)


class LogicContainer(DeclarativeContainer):
    """Logic container."""

    infra_container: p.DependenciesContainer = p.DependenciesContainer()
    serializer: p.Singleton = p.Singleton(EventSerializer)

    event_mediator: p.Singleton = p.Singleton(
        init.init_event_mediator,
        infra_container.websockets_manager,
        infra_container.broker,
        settings.rabbit.message_queue,
        settings.rabbit.message_exchange,
        serializer,
    )
    command_mediator: p.Singleton = p.Singleton(
        init.init_command_mediator,
        event_mediator,
        infra_container.chat_repository,
        infra_container.message_repository,
    )
    mediator: p.Singleton = p.Singleton(
        Mediator,
        event_mediator=event_mediator,
        command_mediator=command_mediator,
    )
    use_cases: p.Singleton = p.Singleton(
        MessageUseCases,
        infra_container.message_repository,
        infra_container.chat_repository,
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
    infra = p.Container(InfraContainer)
    logic = p.Container(LogicContainer, infra_container=infra)
