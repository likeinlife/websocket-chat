import abc
import typing as tp
from collections import defaultdict
from dataclasses import dataclass, field

from logic.commands.entities import BaseCommand
from logic.commands.handlers import BaseCommandHandler

CT = tp.TypeVar("CT", bound=BaseCommand)
CR = tp.TypeVar("CR")


@dataclass
class BaseCommandMediator(abc.ABC, tp.Generic[CT, CR]):
    commands_map: dict[type[CT], list[BaseCommandHandler[CT, CR]]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    @abc.abstractmethod
    def register_command(
        self,
        command: type[CT],
        command_handlers: tp.Iterable[BaseCommandHandler[CT, CR]],
    ) -> None: ...

    @abc.abstractmethod
    async def handle_command(self, command: CT) -> tp.Iterable[CR]: ...
