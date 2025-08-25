from http import HTTPMethod
from typing import IO

import allure
from pydantic import HttpUrl, BaseModel

from httpx import Client, Response, QueryParams

from src.api.authentication.authentication_client import AuthenticationClient
from src.config.settings import settings
from src.schemas.authentication import LoginResponseSchema
from src.schemas.users import LoginRequestSchema


class BasicClient:
    def __init__(self, client: Client):
        self.client = client

    def send_request(
            self,
            method: HTTPMethod,
            url: HttpUrl | str,
            params: QueryParams | None = None,
            json: dict | BaseModel | None = None,
            data: str | None = None,
            files: dict[str, tuple[str, IO[bytes]]] | None = None
    ) -> Response:
        with allure.step(f'Send {method} request to {url}: \n'
                         f'Queries: {params}\n'
                         f'JSON: {json}\n'
                         f'Data: {data}\n'
                         f'Files: {files}'):
            resp = self.client.request(method, url, params=params, json=json, data=data, files=files)
            return resp

    @classmethod
    def get_public_basic_client(cls) -> Client:
        return Client(
            base_url=settings.base_url,
            timeout=settings.timeout
        )

    @classmethod
    def get_private_basic_client(cls) -> Client:
        public_client = cls.get_public_basic_client()
        auth_client = AuthenticationClient.get_public_auth_client()

        login_request = LoginRequestSchema()
        auth_tokens_response = auth_client.authenticate_api(login_request)

        auth_tokens_response_data = auth_tokens_response.json()
        login_response_model = LoginResponseSchema.model_validate_json(auth_tokens_response_data)
        public_client.headers.update(
            {'Authorization': f'{login_response_model.token.token_type} {login_response_model.token.access_token}'})

        return public_client
