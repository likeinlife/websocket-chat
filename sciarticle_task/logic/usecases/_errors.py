from dataclasses import dataclass

from logic.errors import LogicError


class UseCaseError(LogicError):
    """Base use case error."""

    @property
    def message(self) -> str:
        return "Use case error"


@dataclass
class ChatNotFoundError(UseCaseError):
    """Requested chat not found."""

    chat_id: str

    @property
    def message(self) -> str:
        return "Chat not found"
