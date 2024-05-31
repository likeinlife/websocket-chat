import typing as tp
import uuid
from dataclasses import dataclass


@dataclass
class MediatorResponse:
    id: uuid.UUID
    response: list[tp.Any]
