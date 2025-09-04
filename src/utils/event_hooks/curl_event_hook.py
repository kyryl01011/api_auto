import allure
from allure_commons.types import AttachmentType
from httpx import Request

from src.utils.make_curl_from_request import make_curl_from_request


def curl_event_hook(request: Request):
    curl = make_curl_from_request(request)

    allure.attach(curl, name='cURL command', attachment_type=AttachmentType.TEXT)
