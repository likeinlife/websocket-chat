from dataclasses import dataclass

from ._base import BaseEntity


@dataclass
class User(BaseEntity):
    name: str
