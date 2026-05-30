from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.course import Course


def get_all_courses(db: Session) -> list[Course]:
    statement = select(Course)
    return list(db.scalars(statement).all())


def get_course_by_id(db: Session, course_id: int):
    return db.get(Course, course_id)


def create_course(db: Session, course_data: dict):
    course = Course(**course_data)
    db.add(course)
    db.commit()
    db.refresh(course)


def replace_course(db: Session, course_id: int, course_data: dict):
    course = get_course_by_id(db, course_id)
    if course is None:
        return None
    for key, value in course_data.items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course


def update_course(db: Session, course_id: int, course_data: dict):
    course = get_course_by_id(course_id)
    if course is None:
        return None
    for key, value in course_data.items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course


def delete_course(db: Session, course_id: int):
    course = get_course_by_id(db, course_id)
    if course is None:
        return False
    db.delete(course)
    db.commit()
    return True
