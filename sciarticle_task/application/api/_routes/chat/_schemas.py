import datetime as dt
import uuid

from pydantic import BaseModel

from domain.entities import Message


class PostMessageRequest(BaseModel):
    chat_id: str
    text: str


class PostMessageResponse(BaseModel):
    id: uuid.UUID


class UserInfoSchema(BaseModel):
    name: str


class MessageInfoSchema(BaseModel):
    id: uuid.UUID
    chat_id: str
    text: str
    user: UserInfoSchema
    created_at: dt.datetime

    @classmethod
    def from_domain(cls: type["MessageInfoSchema"], message: Message) -> "MessageInfoSchema":
        return cls(
            id=uuid.UUID(message.id),
            chat_id=message.chat_id,
            text=message.text.as_generic_type(),
            user=UserInfoSchema(name=message.user.name),
            created_at=message.created_at,
        )
