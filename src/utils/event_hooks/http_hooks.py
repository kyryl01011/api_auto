from httpx import Request, Response

from src.utils.event_hooks.custom_logger import get_logger


logger = get_logger('HTTP_CLIENT')


def http_request_hook(request: Request):
    logger.info(f'Send {request.method} request to {request.url}')


def http_response_hook(response: Response):
    logger.info(f'Received response status code {response.status_code} from {response.url}')
