import pytest
from httpx import Client

from src.api.get_basic_client import get_public_basic_client, get_private_basic_client
from src.api.users.public_user_client import PublicUserClient


@pytest.fixture
def public_basic_client() -> Client:
    return get_public_basic_client()


@pytest.fixture
def public_user_client() -> PublicUserClient:
    return PublicUserClient.get_public_user_client()


@pytest.fixture
def private_basic_client() -> Client:
    return get_private_basic_client()
