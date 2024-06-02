from faststream.rabbit import RabbitBroker

from domain.entities import Message
from domain.events import NewMessageEvent
from infra.repositories.chats import IChatRepository
from infra.repositories.events import IEventRepository
from infra.repositories.messages import IMessageRepository
from infra.websockets import BaseWebSocketConnectionManager
from logic.commands.entities import CreateMessageCommand
from logic.commands.handlers import CreateMessageCommandHandler
from logic.commands.mediator import CommandMediator
from logic.events.entities import NewMessageFromBrokerEvent
from logic.events.handlers import NewMessageEventHandler, NewMessageFromBrokerEventHandler
from logic.events.mediator import EventMediator
from logic.mediator_pattern import BaseMediator, LoggingEventHandlerProxy
from logic.serializers import BaseEventSerializer


def init_event_mediator(  # noqa: PLR0913
    connection_manager: BaseWebSocketConnectionManager,
    broker: RabbitBroker,
    message_queue: str,
    message_exchange: str,
    event_repository: IEventRepository,
    serializer: BaseEventSerializer,
) -> BaseMediator:
    """Init event mediator."""
    event_mediator = EventMediator()
    event_mediator.register(
        NewMessageFromBrokerEvent,
        LoggingEventHandlerProxy(
            NewMessageFromBrokerEventHandler(
                event_type=NewMessageFromBrokerEvent,
                connection_manager=connection_manager,
            ),
            event_repo=event_repository,
        ),
    )

    event_mediator.register(
        NewMessageEvent,
        LoggingEventHandlerProxy(
            NewMessageEventHandler(
                event_type=NewMessageEvent,
                serializer=serializer,
                broker=broker,
                message_queue=message_queue,
                message_exchange=message_exchange,
            ),
            event_repo=event_repository,
        ),
    )

    return event_mediator


def init_command_mediator(
    event_mediator: EventMediator,
    chat_repository: IChatRepository,
    message_repository: IMessageRepository,
    event_repository: IEventRepository,
) -> BaseMediator:
    """Init command mediator."""
    command_mediator = CommandMediator()
    command_mediator.register(
        CreateMessageCommand,
        LoggingEventHandlerProxy[CreateMessageCommand, Message](
            CreateMessageCommandHandler(
                event_type=CreateMessageCommand,
                event_mediator=event_mediator,
                chats_repository=chat_repository,
                message_repository=message_repository,
            ),
            event_repo=event_repository,
        ),
    )

    return command_mediator
