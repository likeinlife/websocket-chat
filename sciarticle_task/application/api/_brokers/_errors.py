from dataclasses import dataclass

from domain.errors import BaseError


@dataclass
class UnexpectedMessageError(BaseError):
    event_type: str

    @property
    def message(self) -> str:
        return f"Unexpected event type: {self.event_type}"
