from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, HTTPException, status
from faststream.rabbit.fastapi import RabbitRouter

from application.api.dependencies import user
from container import Container
from domain.entities import User
from logic.commands.entities import CreateMessageCommand
from logic.interactors import MessageInteractor
from logic.mediator import Mediator
from logic.usecases import ChatNotFoundError

from ._schemas import MessageInfoSchema, PostMessageRequest, PostMessageResponse

router = RabbitRouter()


@router.post(
    "/",
    summary="Post message to chat room",
    responses={
        status.HTTP_201_CREATED: {"model": PostMessageResponse},
    },
)
@inject
async def post_message(
    body: PostMessageRequest,
    user: User = Depends(user.get_user),
    mediator: Mediator = Depends(Provide[Container.logic.mediator]),
) -> PostMessageResponse:
    result = await mediator.command_mediator.handle(
        CreateMessageCommand(chat_id=body.chat_id, message_text=body.text, user=user),
    )
    return PostMessageResponse(id=UUID(result.id))


@router.get("/message/{message_id}/", summary="Fetch message info")
@inject
async def fetch_message(
    message_id: str,
    message_interactor: MessageInteractor = Depends(Provide[Container.logic.message_interactor]),
) -> MessageInfoSchema:
    result = await message_interactor.fetch_message(message_id=message_id)
    if not result:
        raise HTTPException(status_code=404, detail="Message not found")

    return MessageInfoSchema.from_domain(result)


@router.get("/{chat_id}/", summary="Fetch chat messages")
@inject
async def fetch_chat_messages(
    chat_id: str,
    message_interactor: MessageInteractor = Depends(Provide[Container.logic.message_interactor]),
) -> list[MessageInfoSchema]:
    try:
        result = await message_interactor.fetch_chat_messages(chat_id=chat_id)
        return [MessageInfoSchema.from_domain(message) for message in result]
    except ChatNotFoundError:
        raise HTTPException(status_code=404, detail="Chat not found")  # noqa: B904
