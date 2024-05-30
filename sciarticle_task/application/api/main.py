"""FastAPI entrypoint."""

import typing as tp
from contextlib import asynccontextmanager

from core import settings
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from . import _container_setup, _error_handler, _middlewares, _routes


@asynccontextmanager
async def _lifespan(app: FastAPI) -> tp.AsyncGenerator:  # noqa: ARG001
    container = _container_setup.init_container()
    yield
    _container_setup.shutdown_container(container)


app = FastAPI(
    title=settings.app.name,
    version=settings.app.version,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=_lifespan,
)

_routes.register(app)
_middlewares.register(app)
_error_handler.register(app)
