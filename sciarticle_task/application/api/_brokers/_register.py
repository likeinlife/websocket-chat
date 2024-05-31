from aiojobs import Scheduler
from container import Container
from core import settings
from dependency_injector.wiring import Provide, inject
from faststream.rabbit import RabbitBroker, RabbitExchange, RabbitQueue
from infra.brokers import init_faststream

from ._consumer import message_consumer


@inject
async def register(
    scheduler: Scheduler = Provide[Container.infra.scheduler],
    broker: RabbitBroker = Provide[Container.infra.broker],
) -> None:
    await broker.connect()
    await init_faststream(broker, scheduler)

    message_queue = RabbitQueue(settings.rabbit.message_queue)
    message_exchange = RabbitExchange(settings.rabbit.message_exchange)
    broker.subscriber(message_queue, message_exchange)(message_consumer)
