import typing as tp
import uuid
from dataclasses import dataclass

from domain.events import BaseEvent
from infra.repositories.events import IEventRepository

from ._interface import IUseCase


@dataclass(slots=True)
class FetchEventList(IUseCase[tp.Iterable[BaseEvent]]):
    event_repo: IEventRepository

    async def __call__(self) -> tp.Iterable[BaseEvent]:
        return await self.event_repo.fetch_list()


@dataclass(slots=True)
class FetchEventByID(IUseCase[BaseEvent | None]):
    event_repo: IEventRepository
    event_id: uuid.UUID

    async def __call__(self) -> BaseEvent | None:
        return await self.event_repo.fetch(event_id=self.event_id)
