import uuid

from pydantic import BaseModel


class PostMessageResponse(BaseModel):
    id: uuid.UUID
