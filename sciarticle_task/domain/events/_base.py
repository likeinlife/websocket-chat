from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from uuid import (
    UUID,
    uuid4,
)


@dataclass
class BaseEvent:
    event_id: UUID = field(default_factory=uuid4, kw_only=True)
    occurred_at: datetime = field(default_factory=datetime.now, kw_only=True)
