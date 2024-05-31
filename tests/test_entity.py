from domain.entities import Chat, Message, User
from domain.values import Text


def test_normal():
    message = Message("1", Text("normal"), User(name="UserName"))
    chat = Chat(id="1")

    chat.add_message(message)

    assert len(chat.pull_events()) == 1
