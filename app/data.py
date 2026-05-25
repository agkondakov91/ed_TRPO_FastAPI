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
