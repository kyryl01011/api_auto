from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

from src.utils.get_root_dir import get_root_dir

# env_path = next((p / ".env" for p in Path(__file__).resolve().parents if (p / ".env").exists()), None)
# env_path = get_root_dir() / '.env'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    base_url: str
    host: str
    api_ver: str
    timeout: int

    @property
    def client_url(self):
        return f'{self.base_url}:{self.host}{self.api_ver}'


settings = Settings()
