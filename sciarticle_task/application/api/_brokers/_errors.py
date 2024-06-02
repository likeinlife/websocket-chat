from dataclasses import dataclass

from domain.errors import BaseError


@dataclass(frozen=True, eq=False)
class UnexpectedMessageError(BaseError):
    event_type: str

    @property
    def message(self) -> str:
        return f"Unexpected event type: {self.event_type}"
