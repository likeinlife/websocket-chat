import typing as tp

from domain.entities import User
from fastapi import Body


def get_user(name: tp.Annotated[str, Body()]) -> User:
    """Get user api dependency."""
    return User(name=name)
