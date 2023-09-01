import pytest

@pytest.fixture(scope="module")
def base_url():
    """
    Fixture providing the base URL for API requests in the test module.

    Returns:
        str: The base URL for API requests.
    """
    return "http://localhost:8080"