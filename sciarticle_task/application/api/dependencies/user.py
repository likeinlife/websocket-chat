from domain.entities import User


def get_user(name: str) -> User:
    """Get user api dependency."""
    return User(name=name)
