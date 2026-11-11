def test_import():
    import galaxy_vision  # noqa: F401 — importing IS the test

def test_import_version():
    import galaxy_vision
    assert galaxy_vision.__version__ == "0.1.0"


