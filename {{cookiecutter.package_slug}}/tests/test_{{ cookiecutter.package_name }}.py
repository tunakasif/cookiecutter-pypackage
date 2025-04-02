import {{ cookiecutter.package_name }}


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance({{ cookiecutter.package_name }}.__name__, str)
