.PHONY: freeze
freeze:
	poetry export -o requirements.txt --without-hashes

.PHONY: lint
lint:
	ruff check sciarticle_task
	mypy sciarticle_task
