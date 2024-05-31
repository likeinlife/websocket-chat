from core import settings
from faststream.rabbit import RabbitBroker, RabbitExchange, RabbitQueue

from ._consumer import message_consumer


def register(broker: RabbitBroker) -> None:
    message_queue = RabbitQueue(settings.rabbit.message_queue)
    message_exchange = RabbitExchange(settings.rabbit.message_exchange)
    broker.subscriber(message_queue, message_exchange)(message_consumer)
