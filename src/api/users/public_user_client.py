from http import HTTPMethod

from src.api.basic_client import BasicClient
from src.api.get_basic_client import get_public_basic_client
from src.enums.api_routes import ApiRoutes
from src.schemas.users import CreateUserRequestSchema, GetUserResponseSchema


class PublicUserClient(BasicClient):
    def create_user(self, user: CreateUserRequestSchema) -> GetUserResponseSchema:
        resp = self.client.request(HTTPMethod.POST, ApiRoutes.USER_CREATE.value, json=user.model_dump())
        return GetUserResponseSchema(**resp.json())

    @classmethod
    def get_public_user_client(cls) -> 'PublicUserClient':
        public_client = get_public_basic_client()
        return cls(public_client)
