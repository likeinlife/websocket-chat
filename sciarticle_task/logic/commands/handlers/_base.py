import abc
import typing as tp
from dataclasses import dataclass

from logic.commands.entities import BaseCommand
from logic.events.mediators import BaseEventMediator

CR = tp.TypeVar("CR")


@dataclass
class BaseCommandHandler(abc.ABC, tp.Generic[CR]):
    _mediator: BaseEventMediator

    @abc.abstractmethod
    async def handle(self, command: BaseCommand) -> CR: ...
