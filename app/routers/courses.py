from fastapi import APIRouter, HTTPException, status

from app.data import courses

router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)


@router.get('/')
def get_courses(active: bool | None = None):
    if active is None:
        return courses
    filtered_courses = []
    for course in courses:
        if course['is_active'] == active:
            filtered_courses.append(course)
    return filtered_courses


@router.get('/{course_id}')
def get_course(course_id: int):
    for course in courses:
        if course['id'] == course_id:
            return course
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_course(title: str, description: str):
    new_course = {
        'id': len(courses) + 1,
        'title': title,
        'description': description,
        'is_active': True,
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


@router.patch('/{course_id}')
def partially_update_course(
    course_id: int,
    title: str | None = None,
    description: str | None = None,
    is_active: bool | None = None,
):
    for course in courses:
        if course['id'] == course_id:
            if title is not None:
                course['title'] = title

            if description is not None:
                course['description'] = description

            if is_active is not None:
                course['is_active'] = is_active

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
