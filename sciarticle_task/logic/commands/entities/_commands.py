from dataclasses import dataclass

from ._base import BaseCommand


@dataclass
class CreateMessageCommand(BaseCommand):
    message_text: str
    chat_id: str
