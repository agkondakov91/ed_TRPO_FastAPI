from sqlalchemy import Boolean, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine('sqlite:///./app.db', echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

session = SessionLocal()

try:
    course = Course(
        title='Основы Python',
        description='Базовый курс для начинающих Python-разработчиков',
        is_active=True,
    )

    session.add(course)
    session.commit()
    session.refresh(course)

    print(f'Создан курс: {course.id} — {course.title}')

    statement = select(Course)
    courses: list[Course] = list(session.scalars(statement).all())

    print('Курсы в базе:')

    for course in courses:
        print(f'{course.id}. {course.title} | active={course.is_active}')

finally:
    session.close()
