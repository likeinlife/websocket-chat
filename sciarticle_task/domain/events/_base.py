import typing as tp
import uuid
from datetime import datetime

from pydantic import BaseModel, Field, TypeAdapter

T = tp.TypeVar("T", bound="BaseEvent")


class BaseEvent(BaseModel):
    event_id: uuid.UUID = Field(default_factory=uuid.uuid4, kw_only=True)
    occurred_at: datetime = Field(default_factory=datetime.now, kw_only=True)

    @classmethod
    def from_dict(cls: type[T], data: dict[str, tp.Any]) -> T:
        return TypeAdapter(cls).validate_python(data)
