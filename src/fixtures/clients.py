import pytest

from src.api.authentication.authentication_client import get_authentication_client
from src.api.courses.courses_client import CoursesClient, get_course_client
from src.api.files.files_client import FilesClient, get_files_client
from src.api.public_client_builder import get_public_basic_client
from src.api.private_client_builder import get_private_basic_client
from src.api.users.private_user_client import get_private_user_client
from src.api.users.public_user_client import get_public_user_client
from src.fixtures.users import UserFixtureSchema


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
    return get_files_client(function_user.user_creds)


@pytest.fixture
def courses_client(function_user: UserFixtureSchema) -> CoursesClient:
    return get_course_client(function_user.user_creds)
