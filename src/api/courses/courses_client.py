from http import HTTPMethod

from httpx import Response

from pydantic import UUID4

from src.api.basic_client import BasicClient
from src.api.courses.courses_schema import CreateCourseRequestSchema
from src.api.private_client_builder import get_private_basic_client
from src.enums.api_routes import ApiRoutes
from src.schemas.users import LoginRequestSchema


class CoursesClient(BasicClient):
    def create(self, course: CreateCourseRequestSchema) -> Response:
        resp = self.send_request(
            HTTPMethod.POST,
            ApiRoutes.COURSES_CREATE.value,
            json=course
        )
        return resp

    def get_courses(self, user_id: str) -> Response:
        resp = self.send_request(
            HTTPMethod.GET,
            ApiRoutes.COURSES_GET_ALL.value,
            params={'userId': user_id}
        )
        return resp

    def get(self, course_id: UUID4) -> Response:
        resp = self.send_request(
            HTTPMethod.GET,
            ApiRoutes.COURSES_GET_BY_ID.value(course_id),
        )
        return resp

    def delete(self, course_id: UUID4) -> Response:
        resp = self.send_request(
            HTTPMethod.DELETE,
            ApiRoutes.COURSES_DELETE_BY_ID.value(course_id)
        )
        return resp

    def update(self, course_id: UUID4, course: CreateCourseRequestSchema) -> Response:
        resp = self.send_request(
            HTTPMethod.PATCH,
            ApiRoutes.COURSES_UPDATE_BY_ID.value(course_id),
            json=course
        )
        return resp


def get_course_client(user_creds: LoginRequestSchema) -> CoursesClient:
    client = get_private_basic_client(user_creds)
    return CoursesClient(client)
