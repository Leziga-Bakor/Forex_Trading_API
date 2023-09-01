import pytest

@pytest.fixture(scope="module")
def base_url():
    return "ws://localhost:8080/ws"