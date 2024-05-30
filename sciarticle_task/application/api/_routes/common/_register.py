from fastapi import APIRouter

from . import _healthcheck


def register(router: APIRouter) -> None:
    _router = APIRouter(tags=["common"])
    _router.include_router(_healthcheck.router)

    router.include_router(_router)
