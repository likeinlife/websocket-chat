from dataclasses import dataclass

from ._base import BaseQuery


@dataclass
class FetchMessagesQuery(BaseQuery):
    chat_id: str
