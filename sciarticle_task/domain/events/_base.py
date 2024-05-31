import typing as tp
import uuid
from dataclasses import dataclass, field, fields
from datetime import datetime

T = tp.TypeVar("T", bound="BaseEvent")


@dataclass
class BaseEvent:
    event_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    occurred_at: datetime = field(default_factory=datetime.now, kw_only=True)

    @classmethod
    def from_dict(cls: type[T], data: dict[str, tp.Any]) -> T:
        ignore_names = {"event_id", "occurred_at"}
        names = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in names and k not in ignore_names})
