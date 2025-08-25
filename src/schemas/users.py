from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.utils.data_generator import DataGenerator


class LoginRequestSchema(BaseModel):
    model_config = ConfigDict(
        extra='allow'
    )
    email: EmailStr = Field(default_factory=DataGenerator.generate_email())
    password: str = Field(default_factory=lambda length=10: DataGenerator.generate_random_line(length))


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    user: UserSchema


class CreateUserRequestSchema(LoginRequestSchema):
    last_name: str = Field(alias="lastName", default_factory=DataGenerator.generate_name())
    first_name: str = Field(alias="firstName", default_factory=DataGenerator.generate_name())
    middle_name: str = Field(alias="middleName", default_factory=DataGenerator.generate_name())
