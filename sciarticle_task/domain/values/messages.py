from dataclasses import dataclass

from domain import constants

from . import errors
from .base import BaseValueObject


@dataclass
class Text(BaseValueObject[str]):
    """Text value object.

    Validate empty and size.
    """

    def validate(self) -> None:
        if not self.value:
            raise errors.EmptyTextError
        if len(self.value) > constants.MAX_MESSAGE_LEN:
            raise errors.MessageTooLongError(
                max_length=constants.MAX_MESSAGE_LEN,
                input_length=len(self.value),
            )

    def as_generic_type(self) -> str:
        return str(self.value)
