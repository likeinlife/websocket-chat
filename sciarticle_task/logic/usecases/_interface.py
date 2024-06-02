import abc
import typing as tp
from dataclasses import dataclass

R = tp.TypeVar("R")


@dataclass(slots=True)
class IUseCase(abc.ABC, tp.Generic[R]):
    @abc.abstractmethod
    async def __call__(self) -> R:
        """Execute use-case."""
