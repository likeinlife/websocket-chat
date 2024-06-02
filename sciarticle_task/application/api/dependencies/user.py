import typing as tp

from fastapi import Body

from domain.entities import User


def get_user(name: tp.Annotated[str, Body()]) -> User:
    """Get user api dependency."""
    return User(name=name)
