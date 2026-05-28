from app.repositories import course_repository
from app.schemas.course import CoursePostSchema, CourseReplaceSchema, CourseUpdateSchema


def get_courses(active: bool | None = None, search: str | None = None) -> list[dict]:
    courses = course_repository.get_all_courses()
    if active is not None:
        courses = [course for course in courses if course['is_active'] == active]
    if search is not None:
        courses = [
            course for course in courses if search.lower() in course['title'].lower()
        ]
    return courses


def get_course(course_id: int) -> dict | None:
    return course_repository.get_course_by_id(course_id)


def create_course(course_data: CoursePostSchema) -> dict:
    new_course = {
        'title': course_data.title,
        'description': course_data.description,
        'is_active': course_data.is_active,
    }
    return course_repository.create_course(new_course)


def replace_course(course_id: int, course_data: CourseReplaceSchema) -> dict | None:
    new_course_data = course_data.model_dump()
    return course_repository.replace_course(course_id, new_course_data)


def update_course(course_id: int, course_data: CourseUpdateSchema) -> dict | None:
    update_data = course_data.model_dump(exclude_unset=True)
    return course_repository.update_course(course_id, update_data)


def delete_course(course_id: int) -> bool:
    return course_repository.delete_course(course_id)
