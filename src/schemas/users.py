from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.utils.data_generator import data_generator


class LoginRequestSchema(BaseModel):
    email: EmailStr = Field(default_factory=data_generator.generate_email)
    password: str = Field(default_factory=data_generator.generate_random_line)


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    email: EmailStr = Field(default_factory=data_generator.generate_email)
    password: str = Field(default_factory=data_generator.generate_random_line)
    last_name: str = Field(alias="lastName", default_factory=data_generator.generate_name)
    first_name: str = Field(alias="firstName", default_factory=data_generator.generate_name)
    middle_name: str = Field(alias="middleName", default_factory=data_generator.generate_name)
