from http import HTTPMethod

from src.api.basic_client import BasicClient
from src.api.exercises.exercises_schema import CreateExerciseRequestSchema
from src.api.private_client_builder import get_private_basic_client
from src.enums.api_routes import ApiRoutes
from src.schemas.users import LoginRequestSchema


class ExercisesClient(BasicClient):

    def create(self, exercise: CreateExerciseRequestSchema):
        response = self.send_request(HTTPMethod.POST, ApiRoutes.EXERCISES_CREATE.value, json=exercise)
        return response

    def get_all_exercises(self, course_id: str):
        response = self.send_request(
            HTTPMethod.GET,
            ApiRoutes.EXERCISES_GET_ALL.value,
            params={'courseId': course_id})
        return response

    def get(self, exercise_id: str):
        response = self.send_request(HTTPMethod.GET, ApiRoutes.EXERCISES_GET_BY_ID.value(exercise_id))
        return response

    def update(self, exercise_id: str, exercise: CreateExerciseRequestSchema):
        response = self.send_request(
            HTTPMethod.PATCH,
            ApiRoutes.EXERCISES_UPDATE_BY_ID.value(exercise_id),
            json=exercise)
        return response

    def delete(self, exercise_id: str):
        response = self.send_request(HTTPMethod.DELETE, ApiRoutes.EXERCISES_DELETE_BY_ID.value(exercise_id))
        return response


def get_exercises_client(user_creds: LoginRequestSchema):
    authed_client = get_private_basic_client(user_creds)
    return ExercisesClient(authed_client)
