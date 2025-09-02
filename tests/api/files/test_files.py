from http import HTTPStatus

import pytest

from src.api.files.files_client import FilesClient
from src.api.files.files_schema import CreateFileRequestSchema, GetFileResponseSchema
from src.fixtures.files import FileFixtureSchema
from src.utils.data_generator import data_generator


@pytest.mark.files
@pytest.mark.regression
class TestFiles:

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        'file_path',
        (
                ('./src/testdata/files/test.jpg'),
        )
    )
    def test_create_file(self, files_client: FilesClient, file_path: str):
        file_extension = [name for name in file_path.split('/')][-1].split('.')[-1]
        request = CreateFileRequestSchema(
            filename=f'{data_generator.uuid()}.{file_extension}',
            upload_file=file_path)
        response = files_client.create(request)
        response_model = GetFileResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.file.filename == request.filename

    def test_get_file(self, files_client: FilesClient, function_file: FileFixtureSchema):
        response = files_client.get(function_file.response.file.id)
        response_model = GetFileResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.file.filename == function_file.request.filename

    def test_delete_file(self, files_client: FilesClient, function_file: FileFixtureSchema):
        response = files_client.delete(function_file.response.file.id)

        existence_check = files_client.get(function_file.response.file.id)

        assert response.status_code == HTTPStatus.OK
        assert existence_check.status_code == HTTPStatus.NOT_FOUND
