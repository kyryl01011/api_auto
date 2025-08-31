from http import HTTPStatus

import allure
import pytest

from src.api.api_manager import ApiManager
from src.fixtures.users import UserFixtureSchema
from src.schemas.authentication import LoginResponseSchema


@pytest.mark.authentication
@pytest.mark.regression
@allure.feature("Authentication")
class TestAuthentication:

    @pytest.mark.smoke
    @allure.title("Test Login as user")
    def test_login(self, function_user: UserFixtureSchema, api_manager: ApiManager):
        request = function_user.user_creds
        response = api_manager.authentication_client.authenticate_api(request)
        LoginResponseSchema.model_validate(response.json())

        assert response.status_code == HTTPStatus.OK
