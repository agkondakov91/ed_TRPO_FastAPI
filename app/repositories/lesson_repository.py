from typing import cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lesson import Lesson


def get_all_lessons(
    db: Session,
    course_id: int | None = None,
    active: bool | None = None,
    limit: int = 10,
    offset: int = 0,
) -> list[Lesson]:
    statement = select(Lesson)

    if course_id is not None:
        statement = statement.where(Lesson.course_id == course_id)

    if active is not None:
        statement = statement.where(Lesson.is_active.is_(active))

    statement = statement.order_by(Lesson.id).limit(limit).offset(offset)

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
