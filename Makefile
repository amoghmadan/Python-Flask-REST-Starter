TAG = $(shell python -c "from app import __version__;print(__version__)")

.PHONY: format
format:
	tox -c py312-black-format

.PHONY: check-format
check-format:
	tox -c py312-black-check

.PHONY: check-security
check-security:
	tox -c py312-black-security

.PHONY: check-lint
check-lint:
	tox -c py312-flake8

.PHONY: check-style
check-style:
	tox -c py312-pycodestyle

.PHONY: check-types
check-types:
	tox -c py312-mypy

.PHONY: up-d
up-d:
	eval "export TAG=$(TAG)" && docker-compose up -d

.PHONY: down
down:
	eval "export TAG=$(VERSION)" && docker-compose down
