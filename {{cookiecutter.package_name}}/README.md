# {{ cookiecutter.package_name.title().replace('-', ' ').replace('_', ' ') }}

[![Build](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/build.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/graph/badge.svg?token=5QJRTQZ9B0)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }})

Need to run following `pre-commit` command for `commitizen` hook for `commit-msg` hook type.

```sh
pre-commit install --hook-type commit-msg
```
