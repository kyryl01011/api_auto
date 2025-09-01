import logging
from http import HTTPMethod

import allure
from pydantic import BaseModel

from httpx import Client, Response, QueryParams

from httpx._types import RequestFiles, RequestData


class BasicClient:
    def __init__(self, client: Client):
        self.client = client

    def send_request(
            self,
            method: HTTPMethod,
            endpoint: str,
            params: QueryParams | dict | None = None,
            json: dict | BaseModel | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None,
            headers: dict | None = None,
    ) -> Response:
        with allure.step(f'Send {method} request to {endpoint}: \n'
                         f'Queries: {params}\n'
                         f'JSON: {json}\n'
                         f'Data: {data}\n'):
            url = str(self.client.base_url).strip('/') + endpoint
            if isinstance(json, BaseModel):
                json = json.model_dump(by_alias=True)

            resp = self.client.request(
                method=method,
                url=url,
                data=data,
                files=files,
                json=json,
                params=params,
                headers=headers,
            )

            print('[REQUEST] ', resp.request.url)
            print('[REQUEST-data] ', data)
            print('[REQUEST] ', resp.request.method)
            print('[REQUEST] ', resp.request.headers)
            print('[RESPONSE] ', resp.status_code)
            print('[RESPONSE] ', resp.json())

            return resp
