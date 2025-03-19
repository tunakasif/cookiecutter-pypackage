# {{ cookiecutter.package_name.title().replace('-', ' ').replace('_', ' ') }}

[![Build](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/build.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/graph/badge.svg?token=XXX)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }})

You can initialize the project with `git`, generate virtual environment and install dependencies with `uv` by running:

```sh
make install
```
