from fastapi import FastAPI

from infrastructure.config import settings
from infrastructure.logger import setup_logging

from presentation.api.v1 import api_v1_router


setup_logging(config_file=settings.LOGGING_CONFIG_PATH)
app = FastAPI(
    title=settings.PROJECT_NAME,
)


app.include_router(api_v1_router)
