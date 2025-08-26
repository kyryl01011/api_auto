from enum import Enum


class ApiRoutes(Enum):
    AUTH_LOGIN = '/authentication/login'
    AUTH_REFRESH = '/authentication/refresh'

    USER_GET_ME = '/api/v1/authentication/refresh'
    USER_GET_BY_ID = lambda user_id: f'/api/v1/users/{user_id}'
    USER_UPDATE = lambda user_id: f'/api/v1/users/{user_id}'
    USER_DELETE = lambda user_id: f'/api/v1/users/{user_id}'
    USER_CREATE = '/users'
