from fastapi import FastAPI

from . import _validation_error


def register(app: FastAPI) -> None:
    _validation_error.register(app)
