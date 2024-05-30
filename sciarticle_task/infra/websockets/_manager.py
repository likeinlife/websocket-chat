import asyncio
from dataclasses import (
    dataclass,
    field,
)

from fastapi import WebSocket

from ._base import BaseWebSocketConnectionManager


@dataclass
class WebSocketConnectionManager(BaseWebSocketConnectionManager):
    lock_map: dict[str, asyncio.Lock] = field(default_factory=dict)

    async def accept_connection(self, websocket: WebSocket, key: str) -> None:
        await websocket.accept()

        if key not in self.lock_map:
            self.lock_map[key] = asyncio.Lock()

        async with self.lock_map[key]:
            self.connections_map[key].append(websocket)

    async def remove_connection(self, websocket: WebSocket, key: str) -> None:
        async with self.lock_map[key]:
            self.connections_map[key].remove(websocket)

    async def send_all(self, key: str, bytes_: bytes) -> None:
        for websocket in self.connections_map[key]:
            await websocket.send_bytes(bytes_)
