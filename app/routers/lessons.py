from fastapi import APIRouter, status

from app.schemas.lesson import (
    LessonCreateSchema,
    LessonReadSchema,
    LessonReplaceSchema,
    LessonUpdateSchema,
)
from app.services import lesson_service
from app.utils.exceptions import raise_not_found

router = APIRouter(prefix='/lessons', tags=['Lessons'])


@router.get('/', response_model=list[LessonReadSchema])
def get_lessons(course_id: int | None = None):
    return lesson_service.get_lessons(course_id=course_id)


@router.get('/{lesson_id}', response_model=LessonReadSchema)
def get_lesson(lesson_id: int):
    lesson = lesson_service.get_lesson(lesson_id)
    if lesson is None:
        raise_not_found('Lesson')
    return lesson


@router.post('/', response_model=LessonReadSchema, status_code=status.HTTP_201_CREATED)
def create_lesson(lesson_data: LessonCreateSchema):
    return lesson_service.create_lesson(lesson_data)


@router.put('/{lesson_id}', response_model=LessonReadSchema)
def replace_lesson(lesson_id: int, lesson_data: LessonReplaceSchema):
    lesson = lesson_service.replace_lesson(lesson_id, lesson_data)
    if lesson is None:
        raise_not_found('Lesson')
    return lesson


@router.patch('/{lesson_id}', response_model=LessonReadSchema)
def update_lesson(lesson_id: int, lesson_data: LessonUpdateSchema):
    lesson = lesson_service.update_lesson(lesson_id, lesson_data)
    if lesson is None:
        raise_not_found('Lesson')
    return lesson


@router.delete('/{lesson_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lesson(lesson_id: int):
    is_deleted = lesson_service.delete_lesson(lesson_id)
    if not is_deleted:
        raise_not_found('Lesson')
    return None
