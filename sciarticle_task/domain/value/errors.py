from dataclasses import dataclass

from domain import BaseError


class EmptyTextError(BaseError):  # noqa: D101
    @property
    def message(self) -> str:
        return "Empty text"


@dataclass
class TitleTooLongError(BaseError):  # noqa: D101
    title: str

    @property
    def message(self) -> str:
        return f"Title too long: {self.title}"
