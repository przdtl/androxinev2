from typing import Annotated

from pydantic_settings import BaseSettings, SettingsConfigDict

from fastapi import Depends


class Settings(BaseSettings):
    # Common
    PROJECT_NAME: str = "Carte Backend"
    LOGGING_CONFIG_PATH: str = ".logging.yml"

    # DB
    DB_HOST: str = "localhost"
    DB_USER: str = "admin"
    DB_PASS: str = "admin"
    DB_NAME: str = "carte_auth"
    DB_PORT: int = 5432

    @property
    def DB_URL(self) -> str:
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.DB_USER,
            self.DB_PASS,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_NAME,
        )

    model_config = SettingsConfigDict()


def get_settings():
    return Settings()


settings: Settings = get_settings()
