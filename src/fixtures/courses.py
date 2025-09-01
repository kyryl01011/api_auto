import pytest
from pydantic import BaseModel, UUID4

from src.api.courses.courses_client import CoursesClient
from src.api.courses.courses_schema import CreateCourseRequestSchema, GetCourseResponseSchema
from src.fixtures.files import FileFixtureSchema
from src.fixtures.users import UserFixtureSchema


class CourseFixtureSchema(BaseModel):
    request: CreateCourseRequestSchema
    response: GetCourseResponseSchema

    @property
    def course_id(self) -> UUID4:
        return self.response.course.id


@pytest.fixture
def function_course(
        function_user: UserFixtureSchema,
        courses_client: CoursesClient,
        function_file: FileFixtureSchema) -> CourseFixtureSchema:
    request = CreateCourseRequestSchema(
        createdByUserId=function_user.response.user.id,
        previewFileId=function_file.response.file.id
    )
    response = courses_client.create_course(request)
    response_model = GetCourseResponseSchema.model_validate_json(response.text)
    return CourseFixtureSchema(
        request=request,
        response=response_model
    )
