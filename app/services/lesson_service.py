from app.repositories import lesson_repository
from app.schemas.lesson import (
    LessonCreateSchema,
    LessonReplaceSchema,
    LessonUpdateSchema,
)


def get_lessons(course_id: int | None = None, active: bool | None = None) -> list[dict]:
    lessons = lesson_repository.get_all_lessons()
    if course_id is not None:
        lessons = [lesson for lesson in lessons if lesson['course_id'] == course_id]
    if active is not None:
        lessons = [lesson for lesson in lessons if lesson['is_active'] == active]
    return lessons


def get_lesson(lesson_id: int) -> dict | None:
    return lesson_repository.get_lesson_by_id(lesson_id)


def create_lesson(lesson_data: LessonCreateSchema) -> dict:
    new_lesson = {
        'course_id': lesson_data.course_id,
        'title': lesson_data.title,
        'is_active': lesson_data.is_active,
    }
    return lesson_repository.create_lesson(new_lesson)


def replace_lesson(lesson_id: int, lesson_data: LessonReplaceSchema) -> dict | None:
    new_lesson_data = lesson_data.model_dump()
    return lesson_repository.replace_lesson(lesson_id, new_lesson_data)


def update_lesson(lesson_id: int, lesson_data: LessonUpdateSchema) -> dict | None:
    update_data = lesson_data.model_dump(exclude_unset=True)
    return lesson_repository.update_lesson(lesson_id, update_data)


def delete_lesson(lesson_id: int) -> bool:
    return lesson_repository.delete_lesson(lesson_id)
