<!-- markdownlint-disable MD013 -->

# My Cookiecutter-Pypackage

A simple cookiecutter template for general python projects, including:

- CI/CD with Tox, Commitizen and GitHub Actions
- testing with pytest
- test coverage with Codecov
- linting \& formatting with ruff
- security checks with bandit
- dependency management with Poetry
- pre-commit hooks with ruff and mypy
- Makefile for automating common tasks

## Installation

```sh
cookiecutter gh:tunakasif/cookiecutter-pypackage
cd <project_name>/
make install
make all
```

## Tools and Setup

### Tox

Tox is used for automating testing in multiple Python environments. It is configured in the `tox.ini` file.

### GitHub Actions

> [!WARNING]  
> For the GitHub workflow, you must also set `PERSONAL_ACCESS_TOKEN` and `CODECOV_TOKEN` secrets in repository settings, for releases and code coverage report, respectively.

GitHub Actions is used for continuous integration and continuous deployment (CI/CD). The workflow is defined in `.github/workflows/build.yml`.

### Ruff

Ruff is used for linting and formatting the code. Configuration is available in the `pyproject.toml` file under `[tool.ruff]`.

### Makefile

The `Makefile` provides a set of commands to streamline project setup and maintenance. Key commands include:

- `make install`: Initialize the project, install dependencies, and set up pre-commit hooks.
- `make format`: Format the code using Ruff.
- `make lint`: Lint the code using Ruff and MyPy.
- `make security`: Run security checks using Bandit.
- `make test`: Run tests and generate coverage reports using Pytest.
- `make requirements`: Export dependencies to `requirements.txt`.

## CI

For the GitHub workflow, you must also set `PERSONAL_ACCESS_TOKEN` and `CODECOV_TOKEN` secrets in the repository settings.

## Running Tests

To run tests locally, use:

```sh
make test
```

## Linting and Formatting

To lint and format the code, use:

```sh
make lint
make format
```

## Security Checks

To run security checks, use:

```sh
make security
```

## Exporting Requirements

To automatically export the dependencies to `requirements.txt`, use:

```sh
make requirements
```
