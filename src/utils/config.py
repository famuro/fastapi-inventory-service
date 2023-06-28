from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: int

    class Config:
        env_file: str = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
