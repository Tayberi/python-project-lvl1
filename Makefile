install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3.8 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games