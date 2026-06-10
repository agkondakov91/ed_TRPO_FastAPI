from sqlalchemy.orm import Session

from app.models.course import Course
from app.repositories import course_repository
from app.schemas.course import (
    CoursePostSchema,
    CourseReplaceSchema,
    CourseUpdateSchema,
)


def get_courses(
    db: Session, active: bool | None = None, search: str | None = None
) -> list[Course]:
    courses = course_repository.get_all_courses(db)
    if active is not None:
        courses = [course for course in courses if course.is_active == active]
    if search is not None:
        courses = [
            course for course in courses if search.lower() in course.title.lower()
        ]
    return courses


def get_course(db: Session, course_id: int) -> Course | None:
    return course_repository.get_course_by_id(db, course_id)


def get_course_with_lessons(db: Session, course_id: int) -> Course | None:
    return course_repository.get_course_with_lessons(db, course_id)


def create_course(db: Session, course_data: CoursePostSchema) -> Course:
    new_course = {
        'title': course_data.title,
        'description': course_data.description,
        'is_active': course_data.is_active,
    }
    return course_repository.create_course(db, new_course)


def replace_course(
    db: Session, course_id: int, course_data: CourseReplaceSchema
) -> Course | None:
    new_course_data = course_data.model_dump()
    return course_repository.update_course_fields(db, course_id, new_course_data)


def update_course(
    db: Session, course_id: int, course_data: CourseUpdateSchema
) -> Course | None:
    update_data = course_data.model_dump(exclude_unset=True)
    return course_repository.update_course_fields(db, course_id, update_data)


def delete_course(db: Session, course_id: int) -> bool:
    return course_repository.delete_course(db, course_id)
