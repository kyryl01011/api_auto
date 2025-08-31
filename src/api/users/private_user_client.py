from http import HTTPMethod

from httpx import Response

from src.api.basic_client import BasicClient
from src.api.private_client_builder import get_private_basic_client
from src.enums.api_routes import ApiRoutes
from src.schemas.users import LoginRequestSchema


class PrivateUserClient(BasicClient):
    def get_me(self) -> Response:
        resp = self.send_request(HTTPMethod.GET, ApiRoutes.USER_GET_ME.value)
        return resp

    def get_user_by_id(self, user_id: str) -> Response:
        resp = self.send_request(HTTPMethod.GET, ApiRoutes.USER_GET_BY_ID.value(user_id))
        return resp

    def update_user_by_id(self, user_id: str, update_data: dict) -> Response:
        resp = self.send_request(HTTPMethod.PATCH, ApiRoutes.USER_GET_BY_ID.value(user_id), json=update_data)
        return resp

    def delete_user_by_id(self, user_id: str) -> Response:
        resp = self.send_request(HTTPMethod.DELETE, ApiRoutes.USER_GET_BY_ID.value(user_id))
        return resp


def get_private_user_client(user_creds: LoginRequestSchema) -> PrivateUserClient:
    private_client = get_private_basic_client(user_creds)
    return PrivateUserClient(private_client)
