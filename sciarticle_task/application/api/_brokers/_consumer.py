from container import Container
from dependency_injector.wiring import Provide, inject
from domain.events import NewMessageEvent
from logic.events.entities import NewMessageFromBrokerEvent
from logic.mediator import Mediator
from logic.serializer import BaseEventSerializer

from ._errors import UnexpectedMessageError

mediator: Mediator = Provide[Container.logic.mediator]
serializer: BaseEventSerializer = Provide[Container.logic.serializer]


@inject
async def message_consumer(body: dict) -> None:
    event = serializer.deserialize(body)
    if not isinstance(event, NewMessageEvent):
        raise UnexpectedMessageError(event.__class__.__name__)
    await mediator.event_mediator.publish(
        [
            NewMessageFromBrokerEvent(
                message_text=event.message_text,
                chat_id=event.chat_id,
                message_id=event.message_id,
                user_name=event.user_name,
            ),
        ],
    )
