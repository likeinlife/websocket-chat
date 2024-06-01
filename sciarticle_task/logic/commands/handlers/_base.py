import abc
import typing as tp
from dataclasses import dataclass

from logic.commands.entities import BaseCommand
from logic.events.mediators import BaseEventMediator
from logic.mediator_pattern import IMediatorHandler

CR = tp.TypeVar("CR")


@dataclass
class BaseCommandHandler(IMediatorHandler, tp.Generic[CR]):
    _mediator: BaseEventMediator

    @abc.abstractmethod
    async def handle(self, command: BaseCommand) -> CR: ...
