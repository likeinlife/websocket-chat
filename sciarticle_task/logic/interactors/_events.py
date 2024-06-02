import uuid
from dataclasses import dataclass

from domain.events import BaseEvent
from infra.repositories.events import IEventRepository
from logic.usecases import FetchEventByID, FetchEventList


@dataclass(slots=True)
class EventsInteractor:
    event_repo: IEventRepository

    async def fetch_list(self) -> list[BaseEvent]:
        return list(await FetchEventList(event_repo=self.event_repo)())

    async def fetch(self, event_id: uuid.UUID) -> BaseEvent | None:
        return await FetchEventByID(event_repo=self.event_repo, event_id=event_id)()
