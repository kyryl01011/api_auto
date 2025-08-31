from pydantic import Field, BaseModel


class Token(BaseModel):
    token_type: str = Field(default='bearer', alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginResponseSchema(BaseModel):
    token: Token
