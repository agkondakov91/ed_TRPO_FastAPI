from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.course import get_course_filters
from app.schemas.course import (
    CoursePostSchema,
    CourseReadSchema,
    CourseReplaceSchema,
    CourseUpdateSchema,
)
from app.services import course_service
from app.utils.exceptions import raise_not_found

router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)


@router.get('/', response_model=list[CourseReadSchema])
def get_courses(
    filters: dict = Depends(get_course_filters), db: Session = Depends(get_db)
):
    return course_service.get_courses(
        db=db, active=filters['active'], search=filters['search']
    )


@router.get('/{course_id}', response_model=CourseReadSchema)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = course_service.get_course(db, course_id)
    if course is None:
        raise_not_found('Course')
    return course


@router.post('/', response_model=CourseReadSchema, status_code=status.HTTP_201_CREATED)
def create_course(course_data: CoursePostSchema, db: Session = Depends(get_db)):
    return course_service.create_course(db, course_data)


@router.put('/{course_id}', response_model=CourseReadSchema)
def replace_course(
    course_id: int, course_data: CourseReplaceSchema, db: Session = Depends(get_db)
):
    course = course_service.replace_course(db, course_id, course_data)
    if course is None:
        raise_not_found('Course')
    return course


@router.patch('/{course_id}', response_model=CourseReadSchema)
def update_course(
    course_id: int, course_data: CourseUpdateSchema, db: Session = Depends(get_db)
):
    course = course_service.update_course(db, course_id, course_data)
    if course is None:
        raise_not_found('Course')
    return course


@router.delete('/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    is_deleted = course_service.delete_course(db, course_id)
    if not is_deleted:
        raise_not_found('Course')
    return None
