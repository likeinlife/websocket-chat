from dataclasses import (
    dataclass,
    field,
)

from domain import events, value
from domain.entities.base import BaseEntity


@dataclass(eq=False)
class Message(BaseEntity):
    """Message entity with text."""

    chat_id: str
    text: value.Text


@dataclass(eq=False)
class Chat(BaseEntity):
    """Chat entity with title and messages."""

    title: value.Title
    messages: set[Message] = field(default_factory=set, kw_only=True)

    @classmethod
    def create_chat(cls, title: value.Title) -> "Chat":
        new_chat = cls(title=title)
        new_chat.register_event(
            events.NewChatCreatedEvent(
                chat_id=new_chat.id,
                chat_title=new_chat.title.as_generic_type(),
            ),
        )

        return new_chat

    def add_message(self, message: Message) -> None:
        self.messages.add(message)
        self.register_event(
            events.NewMessageEvent(
                message_text=message.text.as_generic_type(),
                chat_id=self.id,
                message_id=message.id,
            ),
        )

    def delete(self) -> None:
        self.is_deleted = True
        self.register_event(events.ChatDeletedEvent(chat_id=self.id))
