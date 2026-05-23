from fastapi import APIRouter, HTTPException, status

from app.data import courses

router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)


@router.get('/')
def get_courses():
    return courses


@router.get('/{course_id}')
def get_course(course_id: int):
    for course in courses:
        if course['id'] == course_id:
            return course
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
    )
