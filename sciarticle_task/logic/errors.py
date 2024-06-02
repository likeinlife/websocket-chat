from dataclasses import dataclass

from domain.errors import BaseError


@dataclass(frozen=True, eq=False)
class LogicError(BaseError):
    """Base logic error."""

    @property
    def message(self) -> str:
        return "Logic error"
