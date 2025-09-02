import pytest
from httpx import Response
from pydantic import BaseModel

from src.api.files.files_client import FilesClient
from src.api.files.files_schema import CreateFileRequestSchema, GetFileResponseSchema
from src.utils.data_generator import data_generator


class FileFixtureSchema(BaseModel):
    request: CreateFileRequestSchema
    response: GetFileResponseSchema


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixtureSchema:
    create_file_request = CreateFileRequestSchema(
        filename=f'{data_generator.uuid()}',
        directory='test_dir',
        upload_file='./src/testdata/files/test.jpg'
    )
    response: Response = files_client.create(create_file_request)
    create_file_response = GetFileResponseSchema.model_validate_json(response.text)
    return FileFixtureSchema(
        request=create_file_request,
        response=create_file_response
    )
