import {{ cookiecutter.__package_name }}


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance({{ cookiecutter.__package_name }}.__name__, str)
