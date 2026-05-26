from fastapi import APIRouter, HTTPException, status

from app.schemas.course import (
    CoursePostSchema,
    CourseReadSchema,
    CourseReplaceSchema,
    CourseUpdateSchema,
)
from app.services import course_service

router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)


@router.get('/', response_model=list[CourseReadSchema])
def get_courses(active: bool | None = None):
    return course_service.get_courses(active=active)


@router.get('/{course_id}', response_model=CourseReadSchema)
def get_course(course_id: int):
    course = course_service.get_course(course_id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
        )
    return course


@router.post('/', response_model=CourseReadSchema, status_code=status.HTTP_201_CREATED)
def create_course(course_data: CoursePostSchema):
    return course_service.create_course(course_data)


@router.put('/{course_id}', response_model=CourseReadSchema)
def replace_course(course_id: int, course_data: CourseReplaceSchema):
    course = course_service.replace_course(course_id, course_data)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
        )
    return course


@router.patch('/{course_id}', response_model=CourseReadSchema)
def update_course(course_id: int, course_data: CourseUpdateSchema):
    course = course_service.update_course(course_id, course_data)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
        )
    return course


@router.delete('/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int):
    is_delete = course_service.delete_course(course_id)
    if not is_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Course not found'
        )
    return None
