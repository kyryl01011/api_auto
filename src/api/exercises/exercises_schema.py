from typing import Any, ClassVar

from pydantic import BaseModel, Field

from src.utils.data_generator import data_generator


class CreateExerciseRequestSchema(BaseModel):
    title: str = Field(default_factory=data_generator.generate_name, min_length=1, max_length=250)
    course_id: str = Field(alias="courseId")
    description: str = Field(default_factory=data_generator.generate_name, min_length=1)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=data_generator.generate_estimated_time)

    max_score: int | None = Field(default_factory=data_generator.generate_max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=data_generator.generate_min_score, alias="minScore")
    order_index: int | None = Field(default=0, alias="orderIndex")


class Exercise(CreateExerciseRequestSchema):
    id: str


class GetExerciseResponseSchema(BaseModel):
    all_exercises: ClassVar[list[Exercise]] = []

    exercise: Exercise

    def model_post_init(self, context: Any, /) -> None:
        self.all_exercises.append(self.exercise)


class GetExercisesResponseSchema(BaseModel):
    exercises: list[Exercise]
