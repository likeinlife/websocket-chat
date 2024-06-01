from dataclasses import dataclass

from .commands.mediator import CommandMediator
from .events.mediators import BaseEventMediator
from .queries.mediators import BaseQueryMediator


@dataclass
class Mediator:
    """Mediator collection."""

    query_mediator: BaseQueryMediator
    event_mediator: BaseEventMediator
    command_mediator: CommandMediator
