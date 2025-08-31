from httpx import Client

from src.config.settings import settings
from src.enums.client_headers import ClientHeaders


def get_public_basic_client() -> Client:
    return Client(
        base_url=settings.client_url,
        timeout=settings.timeout,
        headers=ClientHeaders.BASIC_HEADERS.value.copy()
    )
