from pydantic import BaseModel, HttpUrl, Field

from src.utils.data_generator import data_generator


class CreateFileRequestSchema(BaseModel):
    filename: str = Field(default_factory=data_generator.uuid, max_length=250)
    directory: str = Field(default='tests', max_length=250)
    upload_file: str


class FileSchema(BaseModel):
    id: str
    filename: str = Field(max_length=250)
    directory: str = Field(max_length=250)
    url: HttpUrl = Field(max_length=2083, min_length=1)


class GetFileResponseSchema(BaseModel):
    file: FileSchema
