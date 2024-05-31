import uuid

from pydantic import BaseModel


class PostMessageRequest(BaseModel):
    chat_id: str
    text: str


class PostMessageResponse(BaseModel):
    id: uuid.UUID
