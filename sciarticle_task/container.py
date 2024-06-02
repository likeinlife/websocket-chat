"""DI container."""

import aiojobs
from dependency_injector import providers as p
from dependency_injector.containers import DeclarativeContainer

from core import configure_logging, settings
from infra.brokers import init_rabbitmq_broker
from infra.repositories.chats import InMemoryChatRepository
from infra.repositories.events import InMemoryEventRepository
from infra.repositories.messages import InMemoryMessageRepository
from infra.websockets import WebSocketConnectionManager
from logic import init
from logic.interactors import MessageInteractor
from logic.mediator import Mediator
from logic.serializers import EventSerializer


class InfraContainer(DeclarativeContainer):
    """Brokers container."""

    scheduler: p.Factory = p.Factory(aiojobs.Scheduler)
    broker: p.Singleton = p.Singleton(init_rabbitmq_broker, settings.rabbit.url)
    websockets_manager: p.Singleton = p.Singleton(WebSocketConnectionManager)
    chat_repository: p.Singleton = p.Singleton(InMemoryChatRepository)
    message_repository: p.Singleton = p.Singleton(InMemoryMessageRepository)
    event_repository: p.Singleton = p.Singleton(InMemoryEventRepository)


class LogicContainer(DeclarativeContainer):
    """Logic container."""

    infra_container: p.DependenciesContainer = p.DependenciesContainer()
    serializer: p.Singleton = p.Singleton(EventSerializer)

    event_mediator: p.Singleton = p.Singleton(
        init.init_event_mediator,
        connection_manager=infra_container.websockets_manager,
        broker=infra_container.broker,
        message_queue=settings.rabbit.message_queue,
        message_exchange=settings.rabbit.message_exchange,
        event_repository=infra_container.event_repository,
        serializer=serializer,
    )
    command_mediator: p.Singleton = p.Singleton(
        init.init_command_mediator,
        event_mediator=event_mediator,
        chat_repository=infra_container.chat_repository,
        message_repository=infra_container.message_repository,
        event_repository=infra_container.event_repository,
    )
    mediator: p.Singleton = p.Singleton(
        Mediator,
        event_mediator=event_mediator,
        command_mediator=command_mediator,
    )
    message_interactor: p.Singleton = p.Singleton(
        MessageInteractor,
        message_repo=infra_container.message_repository,
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
