from typing import cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lesson import Lesson

# lessons = [
#     {
#         'id': 1,
#         'course_id': 1,
#         'title': 'Переменные и типы данных',
#         'is_active': True,
#     },
#     {
#         'id': 2,
#         'course_id': 1,
#         'title': 'Условия и циклы',
#         'is_active': False,
#     },
#     {
#         'id': 3,
#         'course_id': 2,
#         'title': 'Первое FastAPI-приложение',
#         'is_active': True,
#     },
# ]


def get_all_lessons(db: Session) -> list[Lesson]:
    statement = select(Lesson)
    lessons = db.scalars(statement).all()
    return list(lessons)


def get_lesson_by_id(db: Session, lesson_id: int) -> Lesson | None:
    lesson = db.get(Lesson, lesson_id)
    return cast(Lesson | None, lesson)


def create_lesson(db: Session, lesson_data: dict) -> Lesson:
    lesson = Lesson(**lesson_data)
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson


def update_lesson_fields(
    db: Session, lesson_id: int, lesson_data: dict
) -> Lesson | None:
    lesson = get_lesson_by_id(db, lesson_id)
    if lesson is None:
        return None
    for key, value in lesson_data.items():
        setattr(lesson, key, value)
    db.commit()
    db.refresh(lesson)
    return lesson


def delete_lesson(db: Session, lesson_id: int) -> bool:
    lesson = get_lesson_by_id(db, lesson_id)
    if lesson is None:
        return False
    db.delete(lesson)
    db.commit()
    return True
