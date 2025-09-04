from httpx import Client

from src.config.settings import settings
from src.enums.client_headers import ClientHeaders
from src.utils.event_hooks.curl_event_hook import curl_event_hook


def get_public_basic_client() -> Client:
    return Client(
        base_url=settings.client_url,
        timeout=settings.timeout,
        headers=ClientHeaders.BASIC_HEADERS.value.copy(),
        event_hooks={'request': [curl_event_hook]}
    )
