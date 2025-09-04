from http import HTTPMethod

import allure
from httpx import Client

from src.api.authentication.authentication_client import get_authentication_client
from src.api.basic_client import BasicClient
from src.api.files.files_schema import CreateFileRequestSchema
from src.api.private_client_builder import get_private_basic_client
from src.config.settings import settings
from src.enums.api_routes import ApiRoutes
from src.schemas.users import LoginRequestSchema


class FilesClient(BasicClient):
    @allure.step('Get file')
    def get(self, file_id: str):
        resp = self.send_request(HTTPMethod.GET, ApiRoutes.FILE_GET_VIEW.value(file_id))
        return resp

    @allure.step('Delete file')
    def delete(self, file_id: str):
        resp = self.send_request(HTTPMethod.DELETE, ApiRoutes.FILE_DELETE_VIEW.value(file_id))
        return resp

    @allure.step('Create file')
    def create(self, request: CreateFileRequestSchema):
        with open(request.upload_file, 'rb') as file:
            resp = self.send_request(
                HTTPMethod.POST,
                ApiRoutes.FILE_CREATE_VIEW.value,
                data={"filename": request.filename, "directory": request.directory},
                files={'upload_file': file},
            )
        return resp


def get_files_client(user_creds: LoginRequestSchema) -> FilesClient:
    authed_client = get_private_basic_client(user_creds)
    return FilesClient(authed_client)
