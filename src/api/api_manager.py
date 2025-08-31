from httpx import Client

from src.api.authentication.authentication_client import AuthenticationClient
from src.api.files.files_client import FilesClient
from src.api.users.private_user_client import PrivateUserClient, get_private_user_client
from src.api.users.public_user_client import PublicUserClient


class ApiManager:
    def __init__(self, client: Client):
        self.client = client
        self.public_user_client = PublicUserClient(self.client)
        self.private_user_client = PrivateUserClient(self.client)
        self.authentication_client = AuthenticationClient(self.client)
        self.files_client = FilesClient(self.client)
