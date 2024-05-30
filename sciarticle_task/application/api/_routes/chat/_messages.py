from container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, status
from logic.commands.entities import CreateMessageCommand
from logic.mediator import Mediator

router = APIRouter(tags=["chat"])


@router.post("/")
@inject
async def post_message(
    chat_id: str,
    text: str,
    mediator: Mediator = Depends(Provide[Container.logic.mediator]),
) -> Response:
    await mediator.command_mediator.handle_command(CreateMessageCommand(chat_id=chat_id, message_text=text))
    return Response(status_code=status.HTTP_201_CREATED)
