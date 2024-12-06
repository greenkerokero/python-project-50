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

run-flat-json:
	poetry run gendiff gendiff/tests/fixtures/flat_file1.json gendiff/tests/fixtures/flat_file2.json

run-flat-yaml:
	poetry run gendiff gendiff/tests/fixtures/flat_file1.yaml gendiff/tests/fixtures/flat_file2.yaml

run-nested-json:
	poetry run gendiff gendiff/tests/fixtures/nested_file1.json gendiff/tests/fixtures/nested_file2.json

run-nested-yaml:
	poetry run gendiff gendiff/tests/fixtures/nested_file1.yaml gendiff/tests/fixtures/nested_file2.yaml

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -v

test-verbose:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
