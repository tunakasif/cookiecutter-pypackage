def test_import():
    """Test that the package can be imported without errors."""
    try:
        import {{ cookiecutter.project_slug }}
    except ImportError as e:
        raise AssertionError("Failed to import the package.") from e
