from application.api.dependencies import user
from container import Container
from dependency_injector.wiring import Provide, inject
from domain.entities import User
from fastapi import Depends
from faststream.rabbit.fastapi import RabbitRouter
from logic.commands.entities import CreateMessageCommand
from logic.mediator import Mediator

from ._schemas import PostMessageRequest, PostMessageResponse

router = RabbitRouter()


@router.post("/", summary="Post message to chat room")
@inject
async def post_message(
    body: PostMessageRequest,
    user: User = Depends(user.get_user),
    mediator: Mediator = Depends(Provide[Container.logic.mediator]),
) -> PostMessageResponse:
    result = await mediator.command_mediator.handle_command(
        CreateMessageCommand(chat_id=body.chat_id, message_text=body.text, user=user),
    )
    return PostMessageResponse(id=result.id)
