import abc
import typing as tp
from collections import defaultdict
from dataclasses import dataclass, field

from logic.commands.entities import BaseCommand
from logic.commands.handlers import BaseCommandHandler

CR = tp.TypeVar("CR")


@dataclass
class BaseCommandMediator(tp.Generic[CR]):
    commands_map: dict[type[BaseCommand], list[BaseCommandHandler[CR]]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    @abc.abstractmethod
    def register_command(
        self,
        command: type[BaseCommand],
        command_handlers: tp.Iterable[BaseCommandHandler[CR]],
    ) -> None: ...

    @abc.abstractmethod
    async def handle_command(self, command: BaseCommand) -> tp.Iterable[CR]: ...
