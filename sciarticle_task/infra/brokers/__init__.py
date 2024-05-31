"""Message brokers."""

from ._rabbitmq import init_rabbitmq_broker

__all__ = ("init_rabbitmq_broker",)
