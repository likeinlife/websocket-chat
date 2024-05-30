from fastapi import APIRouter, FastAPI

from . import chat, common, ws

router = APIRouter(prefix="/api")


def register(app: FastAPI) -> None:
    common.register(router)
    chat.register(router)
    ws.register(router)

    app.include_router(router)
