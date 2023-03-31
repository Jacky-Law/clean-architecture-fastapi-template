
# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up test

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

bash: up
	docker-compose exec app bash

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/unit /tests/integration /tests/e2e

test-unit: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/unit

test-integration: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/integration

test-e2e: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /tests/e2e

logs:
	docker-compose logs app | tail -1000

black:
	black -l 86 $$(find * -name '*.py')

pre-commit-install:
	pre-commit install

pre-commit-update: pre-commit-install
	pre-commit autoupdate

pre-commit-check-all: pre-commit-install
	pre-commit run --all-files

poetry-self-install:
	# curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
	pip install poetry

poetry-setup:
	poetry update && poetry install

poetry-test-all: poetry-setup
	poetry run pytest --cov={{ cookiecutter.service_name }} ./tests

poetry-test-unit: poetry-setup
	poetry run pytest --cov={{ cookiecutter.service_name }} ./tests/unit

poetry-export:
	poetry update && \
	poetry export -o "./requirements.txt" && \
	poetry export -o "./requirements-dev.txt" --with dev
