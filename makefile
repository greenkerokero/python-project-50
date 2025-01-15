install:
	poetry install

build:
	poetry build

make publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

run:
	poetry run gendiff tests/fixtures/nested_file1.json tests/fixtures/nested_file2.json

run2:
	poetry run gendiff -f plain tests/fixtures/nested_file1.json tests/fixtures/nested_file2.json

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -v

test-brief:
	poetry run pytest -v --no-summary

test-verbose:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
