from dataclasses import dataclass

from ._base import BaseEvent


@dataclass
class NewMessageEvent(BaseEvent):
    message_text: str
    message_id: str
    chat_id: str
    user_name: str
