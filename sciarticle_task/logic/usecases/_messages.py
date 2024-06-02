from dataclasses import dataclass

from domain.entities import Message
from infra.repositories.errors import MessageNotFoundError
from infra.repositories.messages import IMessageRepository

from ._interface import IUseCase


@dataclass(slots=True)
class FetchMessageUseCase(IUseCase[Message | None]):
    message_repo: IMessageRepository
    message_id: str

    async def __call__(self) -> Message | None:
        try:
            return await self.message_repo.fetch(message_id=self.message_id)
        except MessageNotFoundError:
            return None
