import typing as tp
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, HTTPException, status
from faststream.rabbit.fastapi import RabbitRouter

from container import Container
from logic.interactors import EventsInteractor
from logic.serializers import BaseEventSerializer

from ._schemas import EventInfoSchema, ListEventInfoSchema

router = RabbitRouter()


@router.get(
    "/",
    summary="Fetch event list",
    responses={status.HTTP_200_OK: {"model": ListEventInfoSchema}},
)
@inject
async def fetch(
    events_interactor: EventsInteractor = Depends(Provide[Container.logic.event_interactor]),
    serializer: BaseEventSerializer = Depends(Provide[Container.logic.serializer]),
) -> list[dict[str, tp.Any]]:
    result = await events_interactor.fetch_list()
    return [serializer.serialize(event) for event in result]


@router.get(
    "/{event_id}/",
    summary="Fetch event info",
    responses={status.HTTP_200_OK: {"model": EventInfoSchema}},
)
@inject
async def fetch_message(
    event_id: UUID,
    events_interactor: EventsInteractor = Depends(Provide[Container.logic.event_interactor]),
    serializer: BaseEventSerializer = Depends(Provide[Container.logic.serializer]),
) -> dict[str, tp.Any]:
    result = await events_interactor.fetch(event_id)
    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    return serializer.serialize(result)
