import pytest
from domain.constants import MAX_MESSAGE_LEN
from domain.values import Text
from domain.values.errors import EmptyTextError, MessageTooLongError


def test_normal():
    value = "normal"
    t = Text(value=value)
    assert t.as_generic_type() == value


def test_length_limit():
    value = "*" * (MAX_MESSAGE_LEN + 1)
    with pytest.raises(MessageTooLongError):
        Text(value=value)


def test_empty_text():
    value = ""
    with pytest.raises(EmptyTextError):
        Text(value=value)
