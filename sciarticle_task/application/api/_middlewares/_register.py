from fastapi import FastAPI

from . import _correlation, _logger


def register(app: FastAPI) -> None:
    _logger.register(app)
    _correlation.register(app)
