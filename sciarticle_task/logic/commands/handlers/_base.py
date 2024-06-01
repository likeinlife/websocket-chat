import typing as tp
from dataclasses import dataclass

from logic.commands.entities import BaseCommand
from logic.events.mediator import EventMediator
from logic.mediator_pattern import IMediatorHandler

CT = tp.TypeVar("CT", bound=BaseCommand)
CR = tp.TypeVar("CR")


@dataclass
class BaseCommandHandler(IMediatorHandler[CT, CR]):
    event_mediator: EventMediator
