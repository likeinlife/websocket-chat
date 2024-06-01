import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class BaseEvent(BaseModel):
    event_id: uuid.UUID = Field(default_factory=uuid.uuid4, kw_only=True)
    occurred_at: datetime = Field(default_factory=datetime.now, kw_only=True)
