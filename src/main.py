from fastapi import FastAPI

from infrastructure.config import settings

from presentation.api.v1.routers import router as api_v1_router


app = FastAPI(
    title=settings.PROJECT_NAME,
)


app.include_router(api_v1_router)
