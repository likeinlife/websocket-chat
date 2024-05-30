from dataclasses import dataclass

from domain import constants

from . import errors
from .base import BaseValueObject


@dataclass(frozen=True)
class Text(BaseValueObject[str]):
    """Text value object.

    Validate empty.
    """

    def validate(self) -> None:
        if not self.value:
            raise errors.EmptyTextError

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Title(BaseValueObject[str]):
    """Title value object.

    Validate empty and too long.
    """

    def validate(self) -> None:
        if not self.value:
            raise errors.EmptyTextError

        if len(self.value) > constants.MAX_TITLE_LEN:
            raise errors.TitleTooLongError(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)
