import typing as tp
from dataclasses import asdict

from domain.events import BaseEvent, NewMessageEvent
from logic.events.entities import NewMessageFromBrokerEvent

from ._base import BaseEventSerializer
from ._errors import NoTypeFieldInEventError, UnknownEventError

T = tp.TypeVar("T", bound=BaseEvent)

event_list: list[type[BaseEvent]] = [NewMessageEvent, NewMessageFromBrokerEvent]

event_dict: dict[str, type[BaseEvent]] = {cls.__name__: cls for cls in event_list}


class EventSerializer(BaseEventSerializer, tp.Generic[T]):
    type_field: tp.Final = "type"

    def serialize(self, event: T) -> dict[str, tp.Any]:
        data = asdict(event)
        return {**data, self.type_field: event.__class__.__name__}

    def deserialize(self, data: dict[str, tp.Any]) -> T:
        event_type = data.get(self.type_field)
        if not event_type:
            raise NoTypeFieldInEventError(self.type_field)
        event = event_dict.get(event_type)
        if not event:
            raise UnknownEventError(event_type)

        return event.from_dict(data)  # type: ignore  # noqa: PGH003
