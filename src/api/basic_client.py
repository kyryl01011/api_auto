from http import HTTPMethod
from typing import IO

import allure
from pydantic import HttpUrl, BaseModel

from httpx import Client, Response, QueryParams



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
