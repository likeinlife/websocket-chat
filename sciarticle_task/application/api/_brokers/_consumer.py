from container import Container
from dependency_injector.wiring import Provide, inject

from domain.events import NewMessageEvent
from logic.events.entities import NewMessageFromBrokerEvent
from logic.mediator import Mediator
from logic.serializers import BaseEventSerializer

mediator: Mediator = Provide[Container.logic.mediator]
serializer: BaseEventSerializer = Provide[Container.logic.serializer]


@inject
async def message_consumer(body: dict) -> None:
    event = serializer.deserialize(body, NewMessageEvent)
    await mediator.event_mediator.handle(
        NewMessageFromBrokerEvent(
            message_text=event.message_text,
            chat_id=event.chat_id,
            message_id=event.message_id,
            user_name=event.user_name,
        ),
    )
