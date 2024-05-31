from dataclasses import dataclass

from domain.errors import BaseError


class SerializerError(BaseError):
    @property
    def message(self) -> str:
        return "Unknown serializer error"


@dataclass
class NoTypeFieldInEventError(SerializerError):
    type_field_name: str

    @property
    def message(self) -> str:
        return "Event doesn't have 'type' field"


@dataclass
class UnknownEventError(SerializerError):
    type_: str

    @property
    def message(self) -> str:
        return f"Unknown type error: {self.type_}"
