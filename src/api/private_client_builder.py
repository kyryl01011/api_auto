from httpx import Client

from src.config.settings import settings
from src.schemas.authentication import LoginResponseSchema
from src.schemas.users import LoginRequestSchema
from src.api.authentication.authentication_client import get_authentication_client
from src.utils.event_hooks.curl_event_hook import curl_event_hook


def get_private_basic_client(user_creds: LoginRequestSchema, no_curl: bool = False) -> Client:
    authentication_client = get_authentication_client()
    user_login_response: LoginResponseSchema = authentication_client.login_and_get_tokens(user_creds)

    return Client(
        base_url=settings.client_url,
        timeout=settings.timeout,
        headers={'Authorization': f'Bearer {user_login_response.token.access_token}'},
        event_hooks={'request': [curl_event_hook]}
    )
