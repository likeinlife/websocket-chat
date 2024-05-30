from dataclasses import dataclass

from domain import BaseError


class EmptyTextError(BaseError):  # noqa: D101
    @property
    def message(self) -> str:
        return "Empty text"


@dataclass
class MessageTooLongError(BaseError):  # noqa: D101
    max_length: int
    input_length: int

    @property
    def message(self) -> str:
        return f"Message too long. Max length: {self.max_length}. Input length: {self.input_length}"
