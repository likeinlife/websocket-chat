from dataclasses import dataclass

from domain.errors import BaseError


class SerializerError(BaseError):
    @property
    def message(self) -> str:
        return "Unknown serializer error"


@dataclass
class UnknownEventTypeError(SerializerError):
    type_: str

    @property
    def message(self) -> str:
        return f"Unknown type error: {self.type_}"
