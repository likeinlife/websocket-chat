"""Domain zone module.

Contain entities, base error.
"""

from . import constants, entities
from ._errors import BaseError

__all__ = ("BaseError", "entities", "constants")
