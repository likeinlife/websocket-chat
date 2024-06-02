from fastapi import APIRouter, FastAPI

from . import chat, common, events, ws
from .common import ERROR_RESPONSE_SCHEMA


def register(app: FastAPI) -> None:
    router = APIRouter(responses={**ERROR_RESPONSE_SCHEMA})  # type: ignore
    common.register(router)
    chat.register(router)
    ws.register(router)
    events.register(router)

    app.include_router(router)
