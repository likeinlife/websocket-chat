"""FastAPI entrypoint."""

import typing as tp
from contextlib import asynccontextmanager

from container import Container
from core import settings
from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from faststream.rabbit import RabbitBroker

from . import _brokers, _container_setup, _error_handler, _middlewares, _routes


@asynccontextmanager
@inject
async def _lifespan(
    app: FastAPI,  # noqa: ARG001
    broker: RabbitBroker = Provide[Container.infra.broker],
) -> tp.AsyncGenerator:
    container = _container_setup.init_container()
    _brokers.register(broker)
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
