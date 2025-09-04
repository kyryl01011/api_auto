from typing import Self
from http import HTTPMethod

import allure
from httpx import Response

from src.api.basic_client import BasicClient
from src.api.public_client_builder import get_public_basic_client
from src.enums.api_routes import ApiRoutes
from src.schemas.users import CreateUserRequestSchema, GetUserResponseSchema


class PublicUserClient(BasicClient):
    @allure.step("Create user")
    def create_user_api(self, user: CreateUserRequestSchema) -> Response:
        resp = self.send_request(HTTPMethod.POST, ApiRoutes.USER_CREATE.value, json=user)
        return resp

    def create_user(self, user: CreateUserRequestSchema) -> GetUserResponseSchema:
        resp = self.create_user_api(user)
        return GetUserResponseSchema(**resp.json())


def get_public_user_client() -> PublicUserClient:
    public_client = get_public_basic_client()
    return PublicUserClient(public_client)
