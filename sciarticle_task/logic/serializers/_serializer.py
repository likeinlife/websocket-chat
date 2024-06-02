import typing as tp

from pydantic import TypeAdapter, ValidationError

from domain.events import BaseEvent

from ._base import BaseEventSerializer
from ._errors import UnknownEventTypeError

T = tp.TypeVar("T", bound=BaseEvent)


class EventSerializer(BaseEventSerializer):
    type_field: tp.Final = "type"

    def serialize(self, event: BaseEvent) -> dict[str, tp.Any]:
        data = event.model_dump(mode="json")
        return {**data, self.type_field: event.__class__.__name__}

    def deserialize(self, data: dict[str, tp.Any], event_type: type[T]) -> T:
        try:
            return TypeAdapter(event_type).validate_python(data)
        except ValidationError as e:
            raise UnknownEventTypeError(event_type.__name__) from e
