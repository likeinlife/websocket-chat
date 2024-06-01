from ._base import BaseEvent


class NewMessageEvent(BaseEvent):
    message_text: str
    message_id: str
    chat_id: str
    user_name: str
