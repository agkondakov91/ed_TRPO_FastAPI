courses = [
    {
        'id': 1,
        'title': 'Основы Python',
        'description': 'Базовый курс для начинающих Python-разработчиков',
        'is_active': True,
    },
    {
        'id': 2,
        'title': 'FastAPI',
        'description': 'Курс по созданию API на Python',
        'is_active': True,
    },
    {
        'id': 3,
        'title': 'Архивный курс по HTML',
        'description': 'Старый курс, который пока скрыт из основной выдачи',
        'is_active': False,
    },
]


def get_all_courses() -> list[dict]:
    return courses


def get_course_by_id(course_id: int) -> dict | None:
    for course in courses:
        if course['id'] == course_id:
            return course
    return None


def create_course(course_data: dict) -> dict:
    new_course = {'id': len(courses) + 1, **course_data}
    courses.append(new_course)
    return new_course


def replace_course(course_id: int, course_data: dict) -> dict | None:
    for index, course in enumerate(courses):
        if course['id'] == course_id:
            updated_course = {'id': course_id, **course_data}
            courses[index] = updated_course
            return updated_course
    return None


def update_course(course_id: int, course_data: dict) -> dict | None:
    course = get_course_by_id(course_id)
    if course is None:
        return None
    for key, value in course_data.items():
        course[key] = value
    return course


def delete_course(course_id: int) -> bool:
    course = get_course_by_id(course_id)
    if course is None:
        return False
    courses.remove(course)
    return True
