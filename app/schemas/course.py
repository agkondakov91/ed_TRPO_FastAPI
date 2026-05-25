from pydantic import BaseModel, Field


class CoursePostSchema(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    is_active: bool = True


class CourseUpdateSchema(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    is_active: bool | None = None


class CourseReadSchema(BaseModel):
    id: int
    title: str
    description: str | None
    is_active: bool
