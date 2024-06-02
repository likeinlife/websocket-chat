from dataclasses import dataclass

from domain.errors import BaseError


@dataclass(frozen=True, eq=False)
class RepositoryError(BaseError):
    """Base repository error."""

    @property
    def message(self) -> str:
        return "Repository error"


@dataclass(frozen=True, eq=False)
class ChatNotFoundError(BaseError):
    """Requested chat not found."""

    chat_id: str

    @property
    def message(self) -> str:
        return f"Chat not found: {self.chat_id}"


@dataclass(frozen=True, eq=False)
class MessageNotFoundError(BaseError):
    """Requested message not found."""

    message_id: str

    @property
    def message(self) -> str:
        return f"Message not found: {self.message_id}"
