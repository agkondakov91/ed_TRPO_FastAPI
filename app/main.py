from fastapi import FastAPI

from app.routers import courses

app = FastAPI(
    title='Learning Platform API',
    description='API для учебной платформы на FastAPI',
    version='0.2.0',
)

app.include_router(courses.router)


@app.get('/')
def read_root():
    return {'message': 'Welcome to Learning Platform API'}


@app.get('/health')
def health_check():
    return {'status': 'ok'}
