PROJECT_DIR = fg_back

CODE = ${PROJECT_DIR} tests

run:
	poetry run python -m ${PROJECT_DIR}

run-uvicorn:
	poetry run uvicorn ${PROJECT_DIR}.__main__:app --reload --host 0.0.0.0 --port 5000

init:
	poetry install

lint:
	poetry run isort ${CODE}
	poetry run black ${CODE}
	poetry run flake8 ${CODE} --count --select=E9,F63,F7,F82 --show-source --statistics

test:
	poetry run pytest -vsx -m "not slow"

test-all:
	poetry run pytest -vsx