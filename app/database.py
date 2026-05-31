from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = 'sqlite:///./app.db'

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


# def get_db() -> Generator[Session]:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
