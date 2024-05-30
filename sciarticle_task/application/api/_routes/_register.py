from fastapi import APIRouter, FastAPI

from . import common

router = APIRouter(prefix="/api")


def register(app: FastAPI) -> None:
    common.register(router)

    app.include_router(router)
