from fastapi import APIRouter

from . import _messages


def register(router: APIRouter) -> None:
    _router = APIRouter(prefix="/chat", tags=["chat"])
    _router.include_router(_messages.router)

    router.include_router(_router)
