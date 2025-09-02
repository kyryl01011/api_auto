from enum import Enum


class DynamicRoutes:
    def __init__(self, route: str):
        self.route = route

    def __call__(self, *args):
        return self.route.format(*args)


class ApiRoutes(Enum):
    AUTH_LOGIN = '/authentication/login'
    AUTH_REFRESH = '/authentication/refresh'

    USER_GET_ME = '/users/me'
    USER_GET_BY_ID = DynamicRoutes('/users/{}')
    USER_UPDATE = DynamicRoutes('/users/{}')
    USER_DELETE = DynamicRoutes('/users/{}')
    USER_CREATE = '/users'

    FILE_GET_VIEW = DynamicRoutes('/files/{}')
    FILE_DELETE_VIEW = DynamicRoutes('/files/{}')
    FILE_CREATE_VIEW = '/files'

    COURSES_CREATE = '/courses'
    COURSES_GET_ALL = '/courses'
    COURSES_GET_BY_ID = DynamicRoutes('/courses/{}')
    COURSES_UPDATE_BY_ID = DynamicRoutes('/courses/{}')
    COURSES_DELETE_BY_ID = DynamicRoutes('/courses/{}')

    EXERCISES_CREATE = '/exercises'
    EXERCISES_GET_ALL = '/exercises'
    EXERCISES_GET_BY_ID = DynamicRoutes('/exercises/{}')
    EXERCISES_UPDATE_BY_ID = DynamicRoutes('/exercises/{}')
    EXERCISES_DELETE_BY_ID = DynamicRoutes('/exercises/{}')
