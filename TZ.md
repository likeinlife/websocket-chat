# Тестовое задание на позицию Backend Junior Python Developer

Требования к стэку: python3, Postgresql, RabbitMQ, FastAPI, sqlalchemy, CI/CD, docker

При успешном прохождение тестового задания, кандидату будет предложена возможность пройти стажировку со сроком от 1 недели до 3 месяцев, в зависимости от уровня, с возможностью дальнейшего трудоустройства.

# Задание

```python
from fastapi import Depends, FastAPI, WebSocket
from pydantic import BaseModel

from faststream.rabbit.fastapi import RabbitRouter, Logger

router = RabbitRouter("amqp://guest:guest@localhost:5672/")

# TODO Необходимо реализовать эндпоинт POST MESSAGE, который отправляет сообщения
# TODO Необходимо реализовать вебсокет, который принимает из верхнего эндпоинта сообщения
# Ремарка 1:  сообщения приходят только в комнату, где может состоять только 2 юзера
# Ремарка 2:  нельзя использовать любые сторонние клиенты к брокеру очередей (в том числе и прямое API), за исключением faststream

@router.websocket('/updates/{room_id}')
async def get_updates(
      websocket: WebSocket,
      user: User = Depends() # Объект получить по токену):
    ...

```