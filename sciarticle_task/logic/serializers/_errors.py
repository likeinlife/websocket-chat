from dataclasses import dataclass

from domain.errors import BaseError


@dataclass(frozen=True, eq=False)
class SerializerError(BaseError):
    @property
    def message(self) -> str:
        return "Unknown serializer error"


@dataclass(frozen=True, eq=False)
class UnknownEventTypeError(SerializerError):
    type_: str

    @property
    def message(self) -> str:
        return f"Unknown type error: {self.type_}"
