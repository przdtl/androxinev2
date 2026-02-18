from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Common
    PROJECT_NAME: str = "AndroxineV2"

    # Auth
    JWT_SECRET_KEY: str = "your_secret_key"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Telegram
    TELEGRAM_BOT_TOKEN: str = "your_bot_token"

    # DB
    DB_HOST: str = "db"
    DB_USER: str = "admin"
    DB_PASS: str = "admin"
    DB_NAME: str = "androxinev2"
    DB_PORT: int = 5432

    # Redis
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str | None = None

    @property
    def DB_URL(self) -> str:
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.DB_USER,
            self.DB_PASS,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_NAME,
        )

    @property
    def REDIS_URL(self) -> str:
        if self.REDIS_PASSWORD:
            return "redis://:{}@{}:{}/{}".format(
                self.REDIS_PASSWORD,
                self.REDIS_HOST,
                self.REDIS_PORT,
                self.REDIS_DB,
            )

        return "redis://{}:{}/{}".format(
            self.REDIS_HOST,
            self.REDIS_PORT,
            self.REDIS_DB,
        )

    model_config = SettingsConfigDict()


settings = Settings()  # type: ignore
