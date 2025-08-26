import pytest

from src.schemas.users import CreateUserRequestSchema, UserSchema, LoginRequestSchema


class FixtureUserSchema:
    request: CreateUserRequestSchema
    response: UserSchema

    @property
    def user_creds(self) -> LoginRequestSchema:
        return LoginRequestSchema(**self.request.model_dump())


@pytest.fixture
def function_user(public_user_client) -> FixtureUserSchema:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return FixtureUserSchema(request=request, response=response)
