from http import HTTPStatus

import pytest

from src.api.courses.courses_client import CoursesClient
from src.api.courses.courses_schema import CreateCourseRequestSchema, GetCourseResponseSchema
from src.fixtures.courses import CourseFixtureSchema
from src.fixtures.files import FileFixtureSchema
from src.fixtures.users import UserFixtureSchema
from src.utils.data_generator import data_generator


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    @pytest.mark.smoke
    def test_create_course(
            self,
            courses_client: CoursesClient,
            function_user: UserFixtureSchema,
            function_file: FileFixtureSchema):
        request = CreateCourseRequestSchema(
            createdByUserId=function_user.response.user.id,
            previewFileId=function_file.response.file.id
        )
        response = courses_client.create_course(request)
        response_model = GetCourseResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.course.title == request.title

    def test_get_all_courses(self, courses_client: CoursesClient, function_user: UserFixtureSchema):
        response = courses_client.get_courses(function_user.response.user.id)

        assert response.status_code == HTTPStatus.OK

    def test_get_course_by_id(self, courses_client: CoursesClient, function_course: CourseFixtureSchema):
        response = courses_client.get_course_by_id(function_course.response.course.id)
        response_model = GetCourseResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.course.title == function_course.request.title

    @pytest.mark.parametrize(
        'update_fields', (
                ({'title': data_generator.generate_name()}),
                ({'description': data_generator.generate_name()}),
        )
    )
    def test_update_course_by_id(
            self,
            courses_client: CoursesClient,
            function_course: CourseFixtureSchema,
            function_user: UserFixtureSchema,
            function_file: FileFixtureSchema,
            update_fields: dict
    ):
        request = CreateCourseRequestSchema(
            createdByUserId=function_user.response.user.id,
            previewFileId=function_file.response.file.id
        ).model_copy(update=update_fields)
        response = courses_client.update_course_by_id(function_course.response.course.id, request)
        response_model = GetCourseResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.course.title == request.title

    def test_delete_course_by_id(self, courses_client: CoursesClient, function_course: CourseFixtureSchema):
        response = courses_client.delete_course_by_id(function_course.response.course.id)
        second_response = courses_client.delete_course_by_id(function_course.response.course.id)

        assert response.status_code == HTTPStatus.OK
        assert second_response.status_code in (HTTPStatus.NO_CONTENT, HTTPStatus.NOT_FOUND)
