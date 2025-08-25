import pytest
from httpx import Client

from src.api.basic_client import BasicClient
from src.api.users.public_user_client import PublicUserClient
from src.schemas.users import LoginRequestSchema, CreateUserRequestSchema, UserSchema


class FixtureUserSchema:
    request: CreateUserRequestSchema
    response: UserSchema

    @property
    def user_creds(self) -> LoginRequestSchema:
        return LoginRequestSchema(**self.request.model_dump())


@pytest.fixture
def public_basic_client() -> Client:
    return BasicClient.get_public_basic_client()


@pytest.fixture
def public_user_client() -> PublicUserClient:
    return PublicUserClient.get_public_user_client()


@pytest.fixture
def function_user(public_user_client) -> FixtureUserSchema:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return FixtureUserSchema(request=request, response=response)


@pytest.fixture
def private_basic_client() -> Client:
    return BasicClient.get_private_basic_client()
