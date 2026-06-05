from sqlalchemy.orm import Session

from app.models.lesson import Lesson
from app.repositories import lesson_repository
from app.schemas.lesson import (
    LessonCreateSchema,
    LessonReplaceSchema,
    LessonUpdateSchema,
)


def get_lessons(
    db: Session, course_id: int | None = None, active: bool | None = None
) -> list[Lesson]:
    lessons = lesson_repository.get_all_lessons(db)
    if course_id is not None:
        lessons = [lesson for lesson in lessons if lesson.course_id == course_id]
    if active is not None:
        lessons = [lesson for lesson in lessons if lesson.is_active == active]
    return lessons


def get_lesson(db: Session, lesson_id: int) -> Lesson | None:
    return lesson_repository.get_lesson_by_id(db, lesson_id)


def create_lesson(db: Session, lesson_data: LessonCreateSchema) -> Lesson:
    new_lesson = {
        'course_id': lesson_data.course_id,
        'title': lesson_data.title,
        'is_active': lesson_data.is_active,
    }
    return lesson_repository.create_lesson(db, new_lesson)


def replace_lesson(
    db: Session, lesson_id: int, lesson_data: LessonReplaceSchema
) -> Lesson | None:
    new_lesson_data = lesson_data.model_dump()
    return lesson_repository.update_lesson_fields(db, lesson_id, new_lesson_data)


def update_lesson(
    db: Session, lesson_id: int, lesson_data: LessonUpdateSchema
) -> Lesson | None:
    update_data = lesson_data.model_dump(exclude_unset=True)
    return lesson_repository.update_lesson_fields(db, lesson_id, update_data)


def delete_lesson(db: Session, lesson_id: int) -> bool:
    return lesson_repository.delete_lesson(db, lesson_id)
