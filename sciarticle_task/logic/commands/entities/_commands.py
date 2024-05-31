from dataclasses import dataclass

from domain.entities import User

from ._base import BaseCommand


@dataclass
class CreateMessageCommand(BaseCommand):
    message_text: str
    chat_id: str
    user: User
