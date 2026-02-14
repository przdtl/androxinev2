from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Common
    PROJECT_NAME: str = "AndroxineV2"

    # DB
    DB_HOST: str = "db"
    DB_USER: str = "admin"
    DB_PASS: str = "admin"
    DB_NAME: str = "androxinev2"
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


settings = Settings()  # type: ignore
