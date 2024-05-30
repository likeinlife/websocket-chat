from dataclasses import dataclass

from domain import BaseError


class RepositoryError(BaseError):
    """Base repository error."""

    @property
    def message(self) -> str:
        return "Repository error"


@dataclass
class ChatNotFoundError(BaseError):
    """Requested chat not found."""

    chat_id: str

    @property
    def message(self) -> str:
        return f"Chat not found: {self.chat_id}"
