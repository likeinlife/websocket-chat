from fastapi import APIRouter, FastAPI

from . import chat, common, ws


def register(app: FastAPI) -> None:
    router = APIRouter()
    common.register(router)
    chat.register(router)
    ws.register(router)

    app.include_router(router)
