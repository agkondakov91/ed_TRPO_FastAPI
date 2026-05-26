from fastapi import FastAPI

from app.core.config import settings
from app.routers import courses, lessons

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


@app.get('/health')
def health_check():
    return {'status': 'ok'}
