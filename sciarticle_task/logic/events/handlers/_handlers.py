from dataclasses import dataclass

import structlog
from faststream.rabbit import RabbitBroker

from domain.events import NewMessageEvent
from infra.websockets import BaseWebSocketConnectionManager
from logic.events.entities import NewMessageFromBrokerEvent
from logic.serializers import BaseEventSerializer

from ._base import BaseEventHandler


@dataclass
class NewMessageEventHandler(BaseEventHandler[NewMessageEvent, None]):
    serializer: BaseEventSerializer
    broker: RabbitBroker
    message_queue: str
    message_exchange: str
    _logger = structlog.getLogger()

    async def handle(self, event: NewMessageEvent) -> None:
        self._logger.debug("Handle new_message_event", chat_id=event.chat_id)
        await self.broker.publish(
            self.serializer.serialize(event),
            self.message_queue,
            self.message_exchange,
        )


@dataclass
class NewMessageFromBrokerEventHandler(BaseEventHandler[NewMessageFromBrokerEvent, None]):
    connection_manager: BaseWebSocketConnectionManager
    _logger = structlog.getLogger()

    async def handle(self, event: NewMessageFromBrokerEvent) -> None:
        self._logger.debug("Handle new_message_from_broker_event", chat_id=event.chat_id)
        return await self.connection_manager.send_all(event.chat_id, event.to_text().encode())
