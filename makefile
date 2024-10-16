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
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -v

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
