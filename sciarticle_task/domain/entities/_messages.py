from dataclasses import (
    dataclass,
    field,
)

from domain import events, values
from domain.entities import BaseEntity

from ._user import User


@dataclass(eq=False)
class Message(BaseEntity):
    """Message entity with text."""

    chat_id: str
    text: values.Text
    user: User


@dataclass(eq=False)
class Chat(BaseEntity):
    """Chat entity with title and messages."""

    messages: set[Message] = field(default_factory=set, kw_only=True)

    def add_message(self, message: Message) -> None:
        self.messages.add(message)
        self.register_event(
            events.NewMessageEvent(
                message_text=message.text.as_generic_type(),
                chat_id=self.id,
                message_id=message.id,
                user_name=message.user.name,
            ),
        )
