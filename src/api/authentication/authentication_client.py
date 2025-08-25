from http import HTTPMethod

from httpx import Response

from src.api.basic_client import BasicClient
from src.schemas.authentication import LoginResponseSchema
from src.schemas.users import LoginRequestSchema


class AuthenticationClient(BasicClient):
    def authenticate_api(self, user_creds: LoginRequestSchema) -> Response:
        resp = self.send_request(
            HTTPMethod.POST,
            f'{self.client.base_url}/authentication/login',
            json=user_creds,
        )
        return resp

    def login_and_get_tokens(self, user_creds: LoginRequestSchema) -> LoginResponseSchema:
        resp = self.authenticate_api(user_creds)
        auth_tokens = resp.json()
        return auth_tokens

    @classmethod
    def get_public_auth_client(cls) -> 'AuthenticationClient':
        public_client = cls.get_public_basic_client()
        return cls(public_client)
