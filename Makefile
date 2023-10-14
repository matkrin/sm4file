default: test typecheck format

test:
	poetry run pytest
typecheck:
	poetry run mypy -p sm4file
typecheck-all:
	poertry run mypy .
format-check:
	poetry run black --check .
format:
	poetry run black .
docs-serve:
	poetry run mkdocs serve
docs-build:
	poetry run mkdocs build
