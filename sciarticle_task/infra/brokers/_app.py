import aiojobs
from faststream import FastStream
from faststream.rabbit import RabbitBroker


async def init_faststream(broker: RabbitBroker, scheduler: aiojobs.Scheduler) -> FastStream:
    app = FastStream(broker=broker)

    await scheduler.spawn(app.run())
    return app
