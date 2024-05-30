import abc
from collections import defaultdict
from dataclasses import (
    dataclass,
    field,
)

from fastapi import WebSocket


@dataclass
class BaseWebSocketConnectionManager(abc.ABC):
    connections_map: dict[str, list[WebSocket]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    @abc.abstractmethod
    async def accept_connection(self, websocket: WebSocket, key: str) -> None:
        """Accept websocket connection."""

    @abc.abstractmethod
    async def remove_connection(self, websocket: WebSocket, key: str) -> None:
        """Remove websocket connection."""

    @abc.abstractmethod
    async def send_all(self, key: str, bytes_: bytes) -> None:
        """Send message to all connections."""
