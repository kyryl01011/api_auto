from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    base_url: str
    host: int
    api_ver: str
    timeout: int

    @property
    def client_url(self):
        return f'{self.base_url}:{self.host}{self.api_ver}'


settings = Settings()
