from app.database import Base, SessionLocal, engine
from app.models.course import Course
from app.repositories import course_repository

_ = Course

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    course_repository.create_course(
        db,
        {
            'title': 'Основы Python',
            'description': 'Базовый курс для начинающих Python-разработчиков',
            'is_active': True,
        },
    )

    course_repository.create_course(
        db,
        {
            'title': 'FastAPI',
            'description': 'Курс по созданию API на Python',
            'is_active': True,
        },
    )

    courses = course_repository.get_all_courses(db)

    print('Курсы в базе:')

    for course in courses:
        print(f'{course.id}. {course.title} | active = {course.is_active}')

    course = course_repository.get_course_by_id(db, 1)

    print('Курс с id=1:')

    if course is not None:
        print(f'{course.id}. {course.title}')
finally:
    db.close()
