from domain.events import BaseEvent
from logic.mediator_pattern import BaseMediator


class EventMediator(BaseMediator[None, None]):
    """Mediator for events.

    Events should not be created by user directly.
    """

    _allow_event_type = BaseEvent

    async def handle(self, event: BaseEvent) -> None:
        result = []

        handlers = self._get_handlers(event)
        result.extend([await handler.handle(event) for handler in handlers])
