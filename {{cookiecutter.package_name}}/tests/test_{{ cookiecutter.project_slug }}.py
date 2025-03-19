import {{ cookiecutter.project_slug }}


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance({{ cookiecutter.project_slug }}.__name__, str)
