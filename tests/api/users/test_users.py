from http import HTTPStatus

import allure
import pytest

from src.api.users.private_user_client import PrivateUserClient
from src.api.users.public_user_client import PublicUserClient
from src.fixtures.users import UserFixtureSchema
from src.schemas.users import GetUserResponseSchema, CreateUserRequestSchema
from src.utils.allure_enums.allure_epics import AllureEpics
from src.utils.allure_enums.allure_features import AllureFeatures
from src.utils.allure_enums.allure_story import AllureStory


@pytest.mark.users
@pytest.mark.regression
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.USERS)
class TestUsers:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title('Create new user')
    def test_create_user(self, public_users_client: PublicUserClient, function_user: UserFixtureSchema):
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request)
        response_model = GetUserResponseSchema.model_validate_json(response.text)

        assert response.status_code in (HTTPStatus.CREATED, HTTPStatus.OK)
        assert request.email == response_model.user.email
        assert request.first_name == response_model.user.first_name
        assert request.middle_name == response_model.user.middle_name
        assert request.last_name == response_model.user.last_name

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title('Get user me')
    def test_get_user_me(self, private_users_client: PrivateUserClient, function_user: UserFixtureSchema):
        response = private_users_client.get_me()
        response_model = GetUserResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert function_user.request.email == response_model.user.email

    @allure.story(AllureStory.GET_ENTITY)
    @allure.title('Get user by id')
    def test_get_user_by_id(self, function_user: UserFixtureSchema, private_users_client: PrivateUserClient):
        response = private_users_client.get_user_by_id(function_user.response.user.id)
        response_model = GetUserResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert function_user.request.email == response_model.user.email
