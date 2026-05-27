lessons = [
    {
        'id': 1,
        'course_id': 1,
        'title': 'Переменные и типы данных',
        'is_active': True,
    },
    {
        'id': 2,
        'course_id': 1,
        'title': 'Условия и циклы',
        'is_active': False,
    },
    {
        'id': 3,
        'course_id': 2,
        'title': 'Первое FastAPI-приложение',
        'is_active': True,
    },
]


def get_all_lessons() -> list[dict]:
    return lessons


def get_lesson_by_id(lesson_id: int) -> dict | None:
    for lesson in lessons:
        if lesson['id'] == lesson_id:
            return lesson
    return None


def create_lesson(lesson_data: dict) -> dict:
    new_lesson = {'id': len(lessons) + 1, **lesson_data}
    lessons.append(new_lesson)
    return new_lesson


def replace_lesson(lesson_id: int, lesson_data: dict) -> dict | None:
    for index, lesson in enumerate(lessons):
        if lesson['id'] == lesson_id:
            updated_lesson = {'id': lesson_id, **lesson_data}
            lessons[index] = updated_lesson
            return updated_lesson
    return None


def update_lesson(lesson_id: int, lesson_data: dict) -> dict | None:
    lesson = get_lesson_by_id(lesson_id)
    if lesson is None:
        return None
    for key, value in lesson_data.items():
        lesson[key] = value
    return lesson


def delete_lesson(lesson_id: int) -> bool:
    lesson = get_lesson_by_id(lesson_id)
    if lesson is None:
        return False
    lessons.remove(lesson)
    return True
