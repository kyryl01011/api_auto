from http import HTTPStatus

import allure
import pytest

from src.api.authentication.authentication_client import AuthenticationClient
from src.fixtures.users import FixtureUserSchema
from src.schemas.authentication import LoginResponseSchema


@pytest.mark.smoke
@pytest.mark.authentication
@pytest.mark.regression
@allure.feature("Authentication")
class TestAuthentication:

    @allure.title("Test Login as user")
    def test_login(self, function_user: FixtureUserSchema, auth_client: AuthenticationClient):
        request = function_user.user_creds
        response = auth_client.authenticate_api(request)

        LoginResponseSchema.model_validate_json(response.json(), strict=True)
        assert response.status_code == HTTPStatus.OK
