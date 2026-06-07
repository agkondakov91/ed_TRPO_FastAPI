from app.database import Base, SessionLocal, engine
from app.models.course import Course
from app.models.lesson import Lesson

_ = Course
_ = Lesson

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

session = SessionLocal()

try:
    course = Course(
        title='Основы Python',
        description='Базовый курс',
        is_active=True,
    )
    session.add(course)
    session.commit()
    session.refresh(course)

    lesson1 = Lesson(
        course_id=course.id,
        title='Переменные и типы данных',
        is_active=True,
    )

    lesson2 = Lesson(
        course_id=course.id,
        title='Условия',
        is_active=True,
    )
    session.add(lesson1)
    session.add(lesson2)
    session.commit()

    saved_course = session.get(Course, course.id)

    if saved_course is not None:
        print(f'Курс: {saved_course.title}')
        print('Уроки курса:')
        for lesson in saved_course.lessons:
            print(f'- {lesson.title}')

    saved_lesson = session.get(Lesson, lesson1.id)

    if saved_lesson is not None:
        print(f'Урок: {saved_lesson.title}')
        print(f'Курс урока: {saved_lesson.course.title}')
finally:
    session.close()
