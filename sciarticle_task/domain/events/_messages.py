from dataclasses import dataclass

from ._base import BaseEvent


@dataclass
class NewMessageEvent(BaseEvent):
    event_title = "New Message Received"

    message_text: str
    message_id: str
    chat_id: str


@dataclass
class NewChatCreatedEvent(BaseEvent):
    title = "New Chat Created"

    chat_id: str
    chat_title: str


@dataclass
class ChatDeletedEvent(BaseEvent):
    title = "Chat Has Been Deleted"

    chat_id: str
