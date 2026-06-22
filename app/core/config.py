from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Learning Platform API'
    app_description: str = 'API для учебной платформы на FastAPI'
    app_version: str = '0.9.0'
    database_url: str = 'sqlite:///./app.db'
    debug: bool = True

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


@lru_cache
def get_settings() -> Settings:
    return Settings()
