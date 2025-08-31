import pytest
from pydantic import BaseModel

from src.api.api_manager import ApiManager
from src.api.authentication.authentication_client import AuthenticationClient
from src.schemas.users import CreateUserRequestSchema, LoginRequestSchema, GetUserResponseSchema


class UserFixtureSchema(BaseModel):
    request: CreateUserRequestSchema
    response: GetUserResponseSchema

    @property
    def user_creds(self) -> LoginRequestSchema:
        return LoginRequestSchema(**self.request.model_dump())


@pytest.fixture(scope="session")
def session_user_generator(api_manager: ApiManager):
    def _user_generator():
        request = CreateUserRequestSchema()
        response = api_manager.public_user_client.create_user(request)
        return UserFixtureSchema(request=request, response=response)

    return _user_generator


@pytest.fixture
def function_user(session_user_generator) -> UserFixtureSchema:
    return session_user_generator()
