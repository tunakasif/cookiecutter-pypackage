PROJECT_NAME:={{cookiecutter.package_name}}
EXECUTER:=uv run

all: format lint{% if cookiecutter.use_mypy %} type{% endif %}{% if cookiecutter.use_security %} security{% endif %}{% if cookiecutter.use_pytest %} test{% endif %}

init:
	git init
	$(EXECUTER) uv sync
	$(EXECUTER) pre-commit install

clean:
	rm -rf .mypy_cache .pytest_cache .coverage htmlcov
	$(EXECUTER) ruff clean

format:
	$(EXECUTER) ruff format .

lint:
	$(EXECUTER) ruff check . --fix

{% if cookiecutter.use_pytest -%}
test:
	$(EXECUTER) pytest --cov-report term-missing --cov-report html --cov $(PROJECT_NAME)/
{%- endif %}

{% if cookiecutter.use_mypy -%}
type:
	$(EXECUTER) mypy .
{%- endif %}

{% if cookiecutter.use_security -%}
security:
	$(EXECUTER) bandit -r $(PROJECT_NAME)/
	$(EXECUTER) pip-audit
{%- endif %}

