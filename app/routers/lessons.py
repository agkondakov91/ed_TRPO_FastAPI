from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.lesson import get_lesson_filters
from app.schemas.lesson import (
    LessonCreateSchema,
    LessonReadSchema,
    LessonReplaceSchema,
    LessonUpdateSchema,
)
from app.services import lesson_service
from app.utils.exceptions import raise_not_found

router = APIRouter(
    prefix='/lessons',
    tags=['Lessons'],
)


@router.get('/', response_model=list[LessonReadSchema])
def get_lessons(
    filters: dict = Depends(get_lesson_filters), db: Session = Depends(get_db)
):
    return lesson_service.get_lessons(
        db=db,
        course_id=filters['course_id'],
        active=filters['active'],
        limit=filters['limit'],
        offset=filters['offset'],
    )


@router.get('/{lesson_id}', response_model=LessonReadSchema)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = lesson_service.get_lesson(db, lesson_id)
    if lesson is None:
        raise_not_found('Lesson')
    return lesson


@router.post('/', response_model=LessonReadSchema, status_code=status.HTTP_201_CREATED)
def create_lesson(lesson_data: LessonCreateSchema, db: Session = Depends(get_db)):
    return lesson_service.create_lesson(db, lesson_data)


@router.put('/{lesson_id}', response_model=LessonReadSchema)
def replace_lesson(
    lesson_id: int, lesson_data: LessonReplaceSchema, db: Session = Depends(get_db)
):
    lesson = lesson_service.replace_lesson(db, lesson_id, lesson_data)
    if lesson is None:
        raise_not_found('Lesson')
    return lesson


@router.patch('/{lesson_id}', response_model=LessonReadSchema)
def update_lesson(
    lesson_id: int, lesson_data: LessonUpdateSchema, db: Session = Depends(get_db)
):
    lesson = lesson_service.update_lesson(db, lesson_id, lesson_data)
    if lesson is None:
        raise_not_found('Lesson')
    return lesson


@router.delete('/{lesson_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lesson(lesson_id: int, db: Session = Depends(get_db)):
    is_deleted = lesson_service.delete_lesson(db, lesson_id)
    if not is_deleted:
        raise_not_found('Lesson')
    return None
