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

run1:
	poetry run gendiff gendiff/tests/fixtures/flat_file1.json gendiff/tests/fixtures/flat_file2.json

run2:
	poetry run gendiff gendiff/tests/fixtures/nested_file1.json gendiff/tests/fixtures/nested_file2.json

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -v

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
