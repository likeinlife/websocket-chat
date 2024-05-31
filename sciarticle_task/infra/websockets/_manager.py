import asyncio
from dataclasses import (
    dataclass,
    field,
)

import structlog
from fastapi import WebSocket

from ._base import BaseWebSocketConnectionManager


@dataclass
class WebSocketConnectionManager(BaseWebSocketConnectionManager):
    lock_map: dict[str, asyncio.Lock] = field(default_factory=dict)
    _logger = structlog.getLogger()

    async def accept_connection(self, websocket: WebSocket, key: str) -> None:
        await websocket.accept()

        if key not in self.lock_map:
            self.lock_map[key] = asyncio.Lock()

        async with self.lock_map[key]:
            self._logger.debug("Accept connection", key=key)
            self.connections_map[key].append(websocket)

    async def remove_connection(self, websocket: WebSocket, key: str) -> None:
        async with self.lock_map[key]:
            self._logger.debug("Remove connection", key=key)
            self.connections_map[key].remove(websocket)

    async def send_all(self, key: str, bytes_: bytes) -> None:
        for websocket in self.connections_map[key]:
            self._logger.debug("Send message", key=key)
            await websocket.send_bytes(bytes_)
