from dataclasses import dataclass

from domain.events import NewMessageEvent
from faststream.rabbit import RabbitBroker
from infra.websockets import BaseWebSocketConnectionManager
from logic.events.entities import NewMessageFromBrokerEvent

from ._base import BaseEventHandler


@dataclass
class NewMessageEventHandler(BaseEventHandler[NewMessageEvent, None, NewMessageEvent]):
    broker: RabbitBroker
    message_queue: str
    message_exchange: str

    async def handle(self, event: NewMessageEvent) -> None:
        await self.broker.publish(
            self.serializer.serialize(event),
            self.message_queue,
            self.message_exchange,
        )


@dataclass
class NewMessageFromBrokerEventHandler(BaseEventHandler[NewMessageFromBrokerEvent, None, NewMessageFromBrokerEvent]):
    connection_manager: BaseWebSocketConnectionManager

    async def handle(self, event: NewMessageFromBrokerEvent) -> None:
        return await self.connection_manager.send_all(event.chat_id, event.to_text().encode())
