import pytest

@pytest.fixture(scope="module")
def base_url():
    """
    Fixture providing the base WebSocket URL for WebSocket API testing in the test module.

    Returns:
        str: The base WebSocket URL for WebSocket API testing.
    """
    return "ws://localhost:8080/ws"