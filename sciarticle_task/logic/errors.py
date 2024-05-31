from domain.errors import BaseError


class LogicError(BaseError):
    """Base logic error."""

    @property
    def message(self) -> str:
        return "Logic error"
