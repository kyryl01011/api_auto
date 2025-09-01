from pydantic import BaseModel, Field, UUID4

from src.api.files.files_schema import FileSchema
from src.schemas.users import UserSchema
from src.utils.data_generator import data_generator


class CreateCourseRequestSchema(BaseModel):
    title: str = Field(default_factory=data_generator.generate_name)
    description: str = Field(default_factory=data_generator.generate_name, min_length=1)
    preview_file_id: UUID4 | str = Field(alias="previewFileId")
    created_by_user_id: UUID4 | str = Field(alias="createdByUserId")

    estimated_time: str | None = Field(default=None, alias="estimatedTime")
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")


class CourseSchema(BaseModel):
    id: str | UUID4
    title: str = Field(max_length=250, min_length=1)
    max_score: int | None = Field(None, alias="maxScore")
    min_score: int | None = Field(None, alias="minScore")
    estimated_time: str | None = Field(None, alias="estimatedTime")
    description: str = Field(default_factory=data_generator.generate_name, min_length=1)
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCourseResponseSchema(BaseModel):
    course: CourseSchema


class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]
