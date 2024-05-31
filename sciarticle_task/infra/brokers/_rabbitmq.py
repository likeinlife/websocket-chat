from faststream.rabbit import RabbitBroker


def init_rabbitmq_broker(rabbitmq_url: str) -> RabbitBroker:
    return RabbitBroker(rabbitmq_url)
