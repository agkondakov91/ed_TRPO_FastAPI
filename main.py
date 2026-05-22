from fastapi import FastAPI

app = FastAPI(
    title="Learning Platform API",
    description="API для учебной платформы на FastAPI",
    version="0.1.0",
)


courses = [
    {
        "id": 1,
        "title": "Основы Python",
        "description": "Базовый курс для начинающих Python-разработчиков",
    },
    {"id": 2, "title": "FastAPI", "description": "Курс по созданию API на Python"},
]


lessons = [
    {"id": 1, "course_id": 1, "title": "Переменные и типы данных"},
    {"id": 2, "course_id": 1, "title": "Условия и циклы"},
    {"id": 3, "course_id": 2, "title": "Первое FastAPI-приложение"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to Learning Platform API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/courses")
def get_courses():
    return courses


@app.get("/lessons")
def get_lessons():
    return lessons


@app.get("/info")
def get_info():
    return {
        "app_name": "Learning Platform API",
        "version": "0.1.0",
        "author": "https://github.com/agkondakov91",
    }
