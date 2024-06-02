from domain.events import NewMessageEvent
from faststream.rabbit import RabbitBroker
from infra.repositories.chats import IChatRepository
from infra.repositories.messages import IMessageRepository
from infra.websockets import BaseWebSocketConnectionManager
from logic.commands.entities import CreateMessageCommand
from logic.commands.handlers import CreateMessageCommandHandler
from logic.commands.mediator import CommandMediator
from logic.events.entities import NewMessageFromBrokerEvent
from logic.events.handlers import NewMessageEventHandler, NewMessageFromBrokerEventHandler
from logic.events.mediator import EventMediator
from logic.mediator_pattern import BaseMediator
from logic.serializers import BaseEventSerializer


def init_event_mediator(
    connection_manager: BaseWebSocketConnectionManager,
    broker: RabbitBroker,
    message_queue: str,
    message_exchange: str,
    serializer: BaseEventSerializer,
) -> BaseMediator:
    """Init event mediator."""
    event_mediator = EventMediator()
    event_mediator.register(
        NewMessageFromBrokerEvent,
        NewMessageFromBrokerEventHandler(
            connection_manager=connection_manager,
        ),
    )

    event_mediator.register(
        NewMessageEvent,
        NewMessageEventHandler(
            serializer=serializer,
            broker=broker,
            message_queue=message_queue,
            message_exchange=message_exchange,
        ),
    )

    return event_mediator


def init_command_mediator(
    event_mediator: EventMediator,
    chat_repository: IChatRepository,
    message_repository: IMessageRepository,
) -> BaseMediator:
    """Init command mediator."""
    command_mediator = CommandMediator()
    command_mediator.register(
        CreateMessageCommand,
        CreateMessageCommandHandler(
            event_mediator,
            chat_repository,
            message_repository,
        ),
    )

    return command_mediator
