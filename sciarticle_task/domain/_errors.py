class BaseError(Exception):
    """Base error."""

    @property
    def message(self) -> str:
        return "Base error message"

    def __str__(self) -> str:
        return self.message
