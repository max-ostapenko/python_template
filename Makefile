.PHONY: test lint docs

test:
	pytest tests/.*

lint:
	black .
	flake8 .

docs:
	sphinx-build -b html docs build/docs

build: test lint docs
