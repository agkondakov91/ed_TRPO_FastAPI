from typing import cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.course import Course


def get_all_courses(db: Session) -> list[Course]:
    statement = select(Course)
    courses = db.scalars(statement).all()
    return list(courses)


def get_course_by_id(db: Session, course_id: int) -> Course | None:
    course = db.get(Course, course_id)
    return cast(Course | None, course)


def create_course(db: Session, course_data: dict) -> Course:
    course = Course(**course_data)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


# def replace_course(course_id: int, course_data: dict) -> dict | None:
#     for index, course in enumerate(courses):
#         if course['id'] == course_id:
#             updated_course = {'id': course_id, **course_data}
#             courses[index] = updated_course
#             return updated_course
#     return None
#
#
# def update_course(course_id: int, course_data: dict) -> dict | None:
#     course = get_course_by_id(course_id)
#     if course is None:
#         return None
#     for key, value in course_data.items():
#         course[key] = value
#     return course
#
#
# def delete_course(course_id: int) -> bool:
#     course = get_course_by_id(course_id)
#     if course is None:
#         return False
#     courses.remove(course)
#     return True
