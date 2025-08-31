import pytest

from src.api.api_manager import ApiManager
from src.api.public_client_builder import get_public_basic_client


@pytest.fixture(scope="session")
def api_manager():
    public_client = get_public_basic_client()
    return ApiManager(public_client)
