from dataclasses import dataclass

from .commands.mediator import CommandMediator
from .events.mediator import EventMediator
from .queries.mediators import BaseQueryMediator


@dataclass
class Mediator:
    """Mediator collection."""

    query_mediator: BaseQueryMediator
    event_mediator: EventMediator
    command_mediator: CommandMediator
