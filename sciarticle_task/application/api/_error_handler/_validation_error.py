from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from domain.errors import BaseError


async def request_validation_exception_handler(_: Request, exc: RequestValidationError) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": jsonable_encoder(exc.errors(), exclude={"url"}),
        },
    )


async def app_error_handler(_: Request, exc: BaseError) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": exc.message,
        },
    )


def register(app: FastAPI) -> None:
    app.exception_handler(RequestValidationError)(request_validation_exception_handler)
    app.exception_handler(BaseError)(app_error_handler)
