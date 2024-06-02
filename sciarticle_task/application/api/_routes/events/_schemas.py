import datetime as dt
import uuid

from pydantic import BaseModel, RootModel


class EventInfoSchema(BaseModel):
    event_id: uuid.UUID
    occurred_at: dt.datetime
    event_type: str


class ListEventInfoSchema(RootModel):
    root: list[EventInfoSchema]
