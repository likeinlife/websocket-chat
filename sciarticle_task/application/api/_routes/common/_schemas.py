import typing as tp

from fastapi import status
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status_code: int
    message: str


ERROR_RESPONSE_SCHEMA: tp.Final = {status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse}}
