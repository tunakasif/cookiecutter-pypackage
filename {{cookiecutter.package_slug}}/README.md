# {{ cookiecutter.package_slug.title().replace('-', ' ').replace('_', ' ') }}

[![Build](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}/actions/workflows/build.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}/actions/workflows/build.yml)
{% if cookiecutter.use_codecov -%}
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}/graph/badge.svg?token=XXX)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }})
{%- endif %}

You can initialize the project with `git`, generate virtual environment and install dependencies with `uv` by running:

```sh
make init
```
