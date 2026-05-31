from fastapi import Depends, FastAPI

from app.core.config import Settings, settings
from app.database import Base, engine
from app.dependencies.settings import get_settings
from app.models.course import Course
from app.models.lesson import Lesson
from app.routers import courses, lessons

_ = Course
_ = Lesson

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
)

app.include_router(courses.router)
app.include_router(lessons.router)


@app.get('/')
def read_root():
    return {'message': 'Welcome to Learning Platform API'}


@app.get('/info')
def get_info(app_settings: Settings = Depends(get_settings)):
    return {
        'title': app_settings.app_title,
        'description': app_settings.app_description,
        'version': app_settings.app_version,
    }


@app.get('/health')
def health_check():
    return {'status': 'ok'}
