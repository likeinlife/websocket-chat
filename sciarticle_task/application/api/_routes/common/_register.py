from fastapi import APIRouter

from . import _healthcheck

router = APIRouter(tags=["common"])


def register(router: APIRouter) -> None:
    router.include_router(_healthcheck.router)
