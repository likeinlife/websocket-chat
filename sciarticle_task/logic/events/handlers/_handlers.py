from domain.events import NewMessageEvent

from ._base import BaseEventHandler


class NewMessageEventHandler(BaseEventHandler[NewMessageEvent, None]):
    async def handle(self, event: NewMessageEvent) -> None:
        return await self.connection_manager.send_all(event.chat_id, event.message_text.encode())
