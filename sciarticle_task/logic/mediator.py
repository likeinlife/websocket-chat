from dataclasses import dataclass

from .commands.mediator import CommandMediator
from .events.mediator import EventMediator


@dataclass
class Mediator:
    """Mediator collection."""

    event_mediator: EventMediator
    command_mediator: CommandMediator
