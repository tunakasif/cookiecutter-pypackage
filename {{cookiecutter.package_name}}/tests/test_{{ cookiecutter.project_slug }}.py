def test_import() -> None:
    """Test that the package can be imported without errors."""
    try:
        import {{ cookiecutter.project_slug }}

        print({{ cookiecutter.project_slug }}.__version__)
    except ImportError as e:
        raise AssertionError("Failed to import the package.") from e
