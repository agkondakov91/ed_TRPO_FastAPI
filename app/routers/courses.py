from fastapi import APIRouter, HTTPException, status

from app.data import courses
from app.schemas.course import CoursePostSchema, CourseReadSchema, CourseUpdateSchema

router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)


@router.get('/', response_model=list[CourseReadSchema])
def get_courses(active: bool | None = None):
    if active is None:
        return courses
    return [course for course in courses if course['is_active'] == active]


@router.get('/{course_id}', response_model=CourseReadSchema)
def get_course(course_id: int):
    for course in courses:
        if course['id'] == course_id:
            return course
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_course(course_schema: CoursePostSchema):
    new_course = {
        'id': len(courses) + 1,
        'title': course_schema.title,
        'description': course_schema.description,
        'is_active': course_schema.is_active,
    }
    courses.append(new_course)
    return new_course


@router.put('/{course_id}')
def update_course(course_id: int, title: str, description: str, is_active: bool):
    for course in courses:
        if course['id'] == course_id:
            course['title'] = title
            course['description'] = description
            course['is_active'] = is_active
            return course
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
    )


@router.patch('/{course_id}', response_model=CourseReadSchema)
def partially_update_course(course_id: int, course_schema: CourseUpdateSchema):
    for course in courses:
        if course['id'] == course_id:
            update_data = course_schema.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                course[key] = value
            return course
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
    )


@router.delete('/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int):
    for course in courses:
        if course['id'] == course_id:
            courses.remove(course)
            return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
    )
