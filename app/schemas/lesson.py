from pydantic import BaseModel, ConfigDict, Field


class LessonCreateSchema(BaseModel):
    course_id: int = Field(ge=1)
    title: str = Field(min_length=3, max_length=100)
    is_active: bool = True


class LessonReplaceSchema(LessonCreateSchema):
    is_active: bool


class LessonUpdateSchema(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    is_active: bool | None = None


class LessonReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    course_id: int
    title: str
    is_active: bool


class LessonShortSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    is_active: bool
