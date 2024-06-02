from fastapi import APIRouter

from . import _events


def register(router: APIRouter) -> None:
    _router = APIRouter(prefix="/events", tags=["events"])
    _router.include_router(_events.router)

    router.include_router(_router)
