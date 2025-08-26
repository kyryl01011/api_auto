from httpx import Client

from src.api.authentication.authentication_client import AuthenticationClient
from src.config.settings import settings
from src.schemas.authentication import LoginResponseSchema
from src.schemas.users import LoginRequestSchema


def get_public_basic_client() -> Client:
    return Client(
        base_url=settings.client_url,
        timeout=settings.timeout
    )


def get_private_basic_client() -> Client:
    public_client = get_public_basic_client()
    auth_client = AuthenticationClient.get_public_auth_client()

    login_request = LoginRequestSchema()
    auth_tokens_response = auth_client.authenticate_api(login_request)

    auth_tokens_response_data = auth_tokens_response.json()
    login_response_model = LoginResponseSchema.model_validate_json(auth_tokens_response_data)
    public_client.headers.update(
        {'Authorization': f'{login_response_model.token.token_type} {login_response_model.token.access_token}'})

    return public_client
