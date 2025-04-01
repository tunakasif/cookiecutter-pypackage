PROJECT_NAME:={{cookiecutter.project_slug}}
EXECUTER:=uv run

all: format lint type security {% if cookiecutter.use_pytest %}test {% endif %}

init:
	git init
	$(EXECUTER) uv sync
	$(EXECUTER) pre-commit install

clean:
	rm -rf .mypy_cache .pytest_cache .coverage htmlcov
	$(EXECUTER) ruff clean

{% if cookiecutter.use_pytest %}test:
	$(EXECUTER) pytest --cov-report term-missing --cov-report html --cov $(PROJECT_NAME)/{% endif %}

format:
	$(EXECUTER) ruff format .

lint:
	$(EXECUTER) ruff check . --fix

type:
	$(EXECUTER) mypy .

security:
	$(EXECUTER) bandit -r $(PROJECT_NAME)/
	$(EXECUTER) pip-audit

