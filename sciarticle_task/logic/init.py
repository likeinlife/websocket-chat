from domain.events import NewMessageEvent
from infra.repositories.chats import IChatRepository
from infra.repositories.messages import IMessageRepository
from infra.websockets import BaseWebSocketConnectionManager
from logic.commands.entities import CreateMessageCommand
from logic.commands.handlers import CreateMessageCommandHandler
from logic.commands.mediators import BaseCommandMediator, CommandMediator
from logic.events.handlers import NewMessageEventHandler
from logic.events.mediators import BaseEventMediator, EventMediator
from logic.queries.entities import FetchMessagesQuery
from logic.queries.handlers import FetchMessagesQueryHandler
from logic.queries.mediators import BaseQueryMediator, QueryMediator


def init_event_mediator(connection_manager: BaseWebSocketConnectionManager) -> BaseEventMediator:
    """Init event mediator."""
    event_mediator = EventMediator()
    event_mediator.register_event(
        NewMessageEvent,
        [
            NewMessageEventHandler(
                connection_manager,
            ),
        ],
    )
    return event_mediator


def init_command_mediator(
    event_mediator: EventMediator,
    chat_repository: IChatRepository,
    message_repository: IMessageRepository,
) -> BaseCommandMediator:
    """Init command mediator."""
    command_mediator = CommandMediator()
    command_mediator.register_command(
        CreateMessageCommand,
        [
            CreateMessageCommandHandler(
                event_mediator,
                chat_repository,
                message_repository,
            ),
        ],
    )
    return command_mediator


def init_query_mediator(
    message_repository: IMessageRepository,
) -> BaseQueryMediator:
    """Init query mediator."""
    query_mediator = QueryMediator()
    query_mediator.register_query(
        FetchMessagesQuery,
        FetchMessagesQueryHandler(
            message_repository,
        ),
    )
    return query_mediator
