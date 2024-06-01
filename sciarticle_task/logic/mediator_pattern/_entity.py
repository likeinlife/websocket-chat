import uuid

from pydantic import BaseModel, Field


class BaseMediatorEntity(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, kw_only=True)
