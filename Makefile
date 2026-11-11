.PHONY: test lint

test:
	.venv/bin/python -m pytest $(CURDIR)/tests -v 

lint:
	.venv/bin/ruff check src tests
