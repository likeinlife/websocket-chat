DC = docker compose
EXEC = docker compose exec -it
LOGS = docker logs
ENV = --env-file docker-compose/.env
APP_FILE = docker-compose/app.yaml
STORAGES_FILE = docker-compose/storages.yaml
APP_CONTAINER = app

.PHONY: freeze
freeze:
	poetry export -o requirements.txt --without-hashes

.PHONY: lint
lint:
	ruff check sciarticle_task
	mypy sciarticle_task

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-local
app-local:
	cd sciarticle_task; uvicorn application.api.main:app --reload

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: all
all:
	${MAKE} storages
	${MAKE} app

.PHONY: down-app
down-app:
	${DC} -f ${APP_FILE} down

.PHONY: down-storages
down-storages:
	${DC} -f ${STORAGES_FILE} down

.PHONY: down-all
down-all:
	${MAKE} down-storages
	${MAKE} down-app
