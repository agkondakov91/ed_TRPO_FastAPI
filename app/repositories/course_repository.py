from typing import cast

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.course import Course


def get_all_courses(db: Session) -> list[Course]:
    statement = select(Course)
    courses = db.scalars(statement).all()
    return list(courses)


def get_course_by_id(db: Session, course_id: int) -> Course | None:
    course = db.get(Course, course_id)
    return cast(Course | None, course)


def get_course_with_lessons(db: Session, course_id: int) -> Course | None:
    statement = (
        select(Course)
        .options(selectinload(Course.lessons))
        .where(Course.id == course_id)
    )
    course = db.scalars(statement).first()
    return course


def create_course(db: Session, course_data: dict) -> Course:
    course = Course(**course_data)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def update_course_fields(
    db: Session, course_id: int, course_data: dict
) -> Course | None:
    course = get_course_by_id(db, course_id)
    if course is None:
        return None
    for key, value in course_data.items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course


def delete_course(db: Session, course_id: int) -> bool:
    course = get_course_by_id(db, course_id)
    if course is None:
        return False
    db.delete(course)
    db.commit()
    return True
