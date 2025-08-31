from http import HTTPMethod

from httpx import Response

from src.api.basic_client import BasicClient
from src.api.public_client_builder import get_public_basic_client
from src.enums.api_routes import ApiRoutes
from src.schemas.authentication import LoginResponseSchema
from src.schemas.users import LoginRequestSchema


class AuthenticationClient(BasicClient):
    def authenticate_api(self, user_creds: LoginRequestSchema) -> Response:
        resp = self.send_request(
            HTTPMethod.POST,
            f'{ApiRoutes.AUTH_LOGIN.value}',
            json=user_creds,
        )
        return resp

    def login_and_get_tokens(self, user_creds: LoginRequestSchema) -> LoginResponseSchema:
        resp = self.authenticate_api(user_creds)
        auth_tokens = resp.json()
        return LoginResponseSchema(**auth_tokens)


def get_authentication_client() -> AuthenticationClient:
    public_client = get_public_basic_client()
    return AuthenticationClient(public_client)
