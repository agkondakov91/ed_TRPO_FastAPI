from fastapi import APIRouter, HTTPException, status

from app.data import lessons

router = APIRouter(prefix='/lessons', tags=['Lessons'])


# GET    /lessons/
@router.get('/')
def get_lessons(active: bool | None = None):
    if active is None:
        return lessons
    return [lesson for lesson in lessons if lesson['is_active'] == active]


# GET    /lessons/{lesson_id}
@router.get('/{lesson_id}')
def get_lesson(lesson_id: int):
    for lesson in lessons:
        if lesson['id'] == lesson_id:
            return lesson
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Lesson not found'
    )


# POST   /lessons/
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_lesson(course_id: int, title: str):
    new_lesson = {
        'id': len(lessons) + 1,
        'course_id': course_id,
        'title': title,
        'is_active': True,
    }
    lessons.append(new_lesson)
    return new_lesson


# PATCH  /lessons/{lesson_id}
@router.patch('/{lesson_id}')
def partially_update_lesson(
    lesson_id: int, title: str | None = None, is_active: bool | None = None
):
    for lesson in lessons:
        if lesson['id'] == lesson_id:
            if title is not None:
                lesson['title'] = title
            if is_active is not None:
                lesson['is_active'] = is_active
            return lesson
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Lesson not found'
    )


# DELETE /lessons/{lesson_id}
@router.delete('/{lesson_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lesson(lesson_id: int):
    for lesson in lessons:
        if lesson['id'] == lesson_id:
            lessons.remove(lesson)
            return None
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Lesson not found'
    )
