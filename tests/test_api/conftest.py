import pytest

@pytest.fixture(scope="module")
def base_url():
    return "http://localhost:8080"