import pytest
from pydantic import BaseModel

from src.api.exercises.exercises_client import ExercisesClient
from src.api.exercises.exercises_schema import CreateExerciseRequestSchema, GetExerciseResponseSchema
from src.fixtures.courses import CourseFixtureSchema


class ExerciseFixtureSchema(BaseModel):
    request: CreateExerciseRequestSchema
    response: GetExerciseResponseSchema

    @property
    def exercise_id(self) -> str:
        return self.response.exercise.id


@pytest.fixture
def function_exercise(function_course: CourseFixtureSchema, exercises_client: ExercisesClient) -> ExerciseFixtureSchema:
    request = CreateExerciseRequestSchema(
        courseId=function_course.course_id
    )
    response = exercises_client.create(request)
    response_model = GetExerciseResponseSchema.model_validate_json(response.text)

    return ExerciseFixtureSchema(
        request=request,
        response=response_model
    )
