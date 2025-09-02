from http import HTTPStatus

import pytest

from src.api.exercises.exercises_client import ExercisesClient
from src.api.exercises.exercises_schema import CreateExerciseRequestSchema, GetExerciseResponseSchema, \
    GetExercisesResponseSchema
from src.fixtures.courses import CourseFixtureSchema
from src.fixtures.exercises import ExerciseFixtureSchema
from src.utils.data_generator import data_generator


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    @pytest.mark.smoke
    def test_create_exercises(self, exercises_client: ExercisesClient, function_course: CourseFixtureSchema):
        request = CreateExerciseRequestSchema(
            courseId=function_course.course_id
        )
        response = exercises_client.create(request)
        response_model = GetExerciseResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.exercise.title == request.title
        assert response_model.exercise.course_id == function_course.course_id

    def test_get_all_exercises(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixtureSchema
    ):
        response = exercises_client.get_all_exercises(function_exercise.response.exercise.course_id)
        response_model = GetExercisesResponseSchema.model_validate_json(response.text)
        exercises_ids = [ex.id for ex in response_model.exercises]

        assert response.status_code == HTTPStatus.OK
        assert function_exercise.exercise_id in exercises_ids

    def test_get_exercise_by_id(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixtureSchema):
        response = exercises_client.get(function_exercise.exercise_id)
        response_model = GetExerciseResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.exercise.title == function_exercise.response.exercise.title

    def test_update_exercise_by_id(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixtureSchema,
            function_course: CourseFixtureSchema
    ):
        request = CreateExerciseRequestSchema(
            courseId=function_course.course_id
        ).model_copy(update={'title': data_generator.generate_name()})
        response = exercises_client.update(function_exercise.exercise_id, request)
        response_model = GetExerciseResponseSchema.model_validate_json(response.text)

        assert response.status_code == HTTPStatus.OK
        assert response_model.exercise.title == request.title
        assert response_model.exercise.id == function_exercise.exercise_id

    def test_delete_exercise_by_id(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixtureSchema,
    ):
        response = exercises_client.delete(function_exercise.exercise_id)
        second_response = exercises_client.get(function_exercise.exercise_id)

        assert response.status_code == HTTPStatus.OK
        assert second_response.status_code in (HTTPStatus.NOT_FOUND, HTTPStatus.NO_CONTENT)
