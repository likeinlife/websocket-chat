from dataclasses import dataclass

from domain.events import BaseEvent


@dataclass
class NewMessageFromBrokerEvent(BaseEvent):
    """New message from broker event."""

    message_text: str
    chat_id: str
    message_id: str
    user_name: str

    def to_text(self) -> str:
        return f"{self.user_name}: {self.message_text}"
