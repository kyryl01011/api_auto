from http import HTTPStatus

from src.api.api_manager import ApiManager
from src.api.users.public_user_client import PublicUserClient
from src.fixtures.users import UserFixtureSchema
from src.schemas.authentication import LoginResponseSchema
from src.schemas.users import GetUserResponseSchema


class TestUsers:
    def test_create_user(self, public_users_client: PublicUserClient, function_user: UserFixtureSchema):
        request = function_user.request
        response = public_users_client.create_user_api(request)
        response_model = GetUserResponseSchema(**response.json())

        assert response.status_code == HTTPStatus.CREATED
        assert request.email == response_model.user.email
        assert request.first_name == response_model.user.first_name
        assert request.middle_name == response_model.user.middle_name
        assert request.last_name == response_model.user.last_name

    def test_get_user_me(self, api_manager: ApiManager, function_user: UserFixtureSchema):
        login_response = api_manager.authentication_client.authenticate_api(function_user.user_creds)
        login_tokens = LoginResponseSchema.model_validate_json(login_response.text)
        api_manager.client.headers.update({"Authorization": f"Bearer {login_tokens.token.access_token}"})

        response = api_manager.private_user_client.get_me()
        response_model = GetUserResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert function_user.request.email == response_model.user.email

    def test_get_user_by_id(self, function_user: UserFixtureSchema, api_manager: ApiManager):
        response = api_manager.private_user_client.get_user_by_id(function_user.response.user.id)
        response_model = GetUserResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert function_user.request.email == response_model.user.email
