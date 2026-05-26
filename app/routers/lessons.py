from fastapi import APIRouter, HTTPException, status

from app.repositories.lesson_repository import lessons
from app.schemas.lesson import LessonCreateSchema, LessonReadSchema, LessonUpdateSchema

router = APIRouter(prefix='/lessons', tags=['Lessons'])


@router.get('/', response_model=list[LessonReadSchema])
def get_lessons(course_id: int | None = None):
    if course_id is None:
        return lessons
    return [lesson for lesson in lessons if lesson['course_id'] == course_id]


@router.get('/{lesson_id}', response_model=LessonReadSchema)
def get_lesson(lesson_id: int):
    for lesson in lessons:
        if lesson['id'] == lesson_id:
            return lesson
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Lesson not found'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_lesson(lesson_schema: LessonCreateSchema):
    new_lesson = {
        'id': len(lessons) + 1,
        'course_id': lesson_schema.course_id,
        'title': lesson_schema.title,
        'is_active': lesson_schema.is_active,
    }
    lessons.append(new_lesson)
    return new_lesson


@router.patch('/{lesson_id}', response_model=LessonReadSchema)
def partially_update_lesson(lesson_id: int, lesson_schema: LessonUpdateSchema):
    for lesson in lessons:
        if lesson['id'] == lesson_id:
            update_data = lesson_schema.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                lesson[key] = value
            return lesson
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Lesson not found'
    )


@router.delete('/{lesson_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lesson(lesson_id: int):
    for lesson in lessons:
        if lesson['id'] == lesson_id:
            lessons.remove(lesson)
            return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Lesson not found'
    )
