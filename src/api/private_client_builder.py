from httpx import Client

from src.api.public_client_builder import get_public_basic_client
from src.schemas.authentication import LoginResponseSchema
from src.schemas.users import LoginRequestSchema
from src.api.authentication.authentication_client import get_authentication_client


def get_private_basic_client(user_creds: LoginRequestSchema) -> Client:
    authentication_client = get_authentication_client()
    public_client = get_public_basic_client()

    user_login_response: LoginResponseSchema = authentication_client.login_and_get_tokens(user_creds)

    public_client.headers.update({'Authorization': f'Bearer {user_login_response.token.access_token}'})
    return public_client
