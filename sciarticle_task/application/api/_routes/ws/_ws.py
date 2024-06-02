from contextlib import suppress

from container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, WebSocket, status

from infra.websockets import WebSocketConnectionManager

router = APIRouter()


@router.websocket("/updates/{room_id}")
@inject
async def get_updates(
    room_id: str,
    websocket: WebSocket,
    websocket_manager: WebSocketConnectionManager = Depends(Provide[Container.infra.websockets_manager]),
) -> Response:
    await websocket_manager.accept_connection(websocket, room_id)

    with suppress(Exception):
        while True:
            await websocket.receive_text()
    await websocket_manager.remove_connection(websocket, room_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
