from fastapi import APIRouter

from . import _ws


def register(router: APIRouter) -> None:
    _router = APIRouter(prefix="/ws", tags=["ws"])
    _router.include_router(_ws.router)

    router.include_router(_router)
