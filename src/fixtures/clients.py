import pytest

from src.api.authentication.authentication_client import get_authentication_client
from src.api.courses.courses_client import CoursesClient, get_course_client
from src.api.courses.courses_schema import GetCourseResponseSchema
from src.api.exercises.exercises_client import ExercisesClient, get_exercises_client
from src.api.exercises.exercises_schema import GetExerciseResponseSchema
from src.api.files.files_client import FilesClient, get_files_client
from src.api.files.files_schema import GetFileResponseSchema
from src.api.public_client_builder import get_public_basic_client
from src.api.private_client_builder import get_private_basic_client
from src.api.users.private_user_client import get_private_user_client
from src.api.users.public_user_client import get_public_user_client
from src.fixtures.users import UserFixtureSchema
from src.utils.fixture_entities_cleaner import fixture_entities_cleanup


@pytest.fixture
def public_client():
    return get_public_basic_client()


@pytest.fixture
def authentication_client():
    return get_authentication_client()


@pytest.fixture
def private_client(function_user: UserFixtureSchema):
    return get_private_basic_client(function_user.user_creds)


@pytest.fixture
def public_users_client():
    return get_public_user_client()


@pytest.fixture
def private_users_client(function_user: UserFixtureSchema):
    return get_private_user_client(function_user.user_creds)


@pytest.fixture
def files_client(function_user: UserFixtureSchema) -> FilesClient:
    client = get_files_client(function_user.user_creds)
    yield client

    for file in GetFileResponseSchema.all_files:
        fixture_entities_cleanup(client, file.id)


@pytest.fixture
def courses_client(function_user: UserFixtureSchema) -> CoursesClient:
    client: CoursesClient = get_course_client(function_user.user_creds)
    yield client

    for course in GetCourseResponseSchema.all_courses:
        fixture_entities_cleanup(client, course.id)


@pytest.fixture
def exercises_client(function_user: UserFixtureSchema) -> ExercisesClient:
    client: ExercisesClient = get_exercises_client(function_user.user_creds)
    yield client

    for exercise in GetExerciseResponseSchema.all_exercises:
        fixture_entities_cleanup(client, exercise.id)
