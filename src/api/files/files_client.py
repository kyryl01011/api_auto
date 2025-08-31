from http import HTTPMethod

from httpx import Client

from src.api.authentication.authentication_client import get_authentication_client
from src.api.basic_client import BasicClient
from src.api.files.files_schema import CreateFileRequestSchema
from src.config.settings import settings
from src.enums.api_routes import ApiRoutes
from src.schemas.users import LoginRequestSchema


class FilesClient(BasicClient):
    def get_file(self, file_id: str):
        resp = self.send_request(HTTPMethod.GET, ApiRoutes.FILE_GET_VIEW.value(file_id))
        return resp

    def delete_file(self, file_id: str):
        resp = self.send_request(HTTPMethod.DELETE, ApiRoutes.FILE_DELETE_VIEW.value(file_id))
        return resp

    def create_file(self, request: CreateFileRequestSchema):
        with open(request.upload_file, 'rb') as file:
            resp = self.send_request(
                HTTPMethod.POST,
                ApiRoutes.FILE_CREATE_VIEW.value,
                data={"filename": request.filename, "directory": request.directory},
                files={'upload_file': file},
            )
        return resp


def get_files_client(user_creds: LoginRequestSchema) -> FilesClient:
    auth_client = get_authentication_client()
    tokens = auth_client.login_and_get_tokens(user_creds)
    return FilesClient(client=Client(
        base_url=settings.client_url,
        timeout=settings.timeout,
        headers={
            'Authorization': f'Bearer {tokens.token.access_token}'
        }
    ))
