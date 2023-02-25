.PHONY: install format lint

install:
	@poetry install
format:
	@isort .
	@blue .
lint:
	@isort . --check
	@blue . --check
	@flake8 --extend-ignore=E501