from container import Container
from dependency_injector.wiring import Provide, inject
from domain.events import NewMessageEvent
from faststream import Depends
from logic.events.entities import NewMessageFromBrokerEvent
from logic.mediator import Mediator


@inject
async def message_consumer(
    body: NewMessageEvent,
    mediator: Mediator = Depends(Provide[Container.logic.mediator]),
) -> None:
    await mediator.event_mediator.publish(
        [
            NewMessageFromBrokerEvent(
                message_text=body.message_text,
                chat_id=body.chat_id,
                message_id=body.message_id,
            ),
        ],
    )
