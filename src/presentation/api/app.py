from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings

from presentation.telegram import setup_webhook, shutdown_webhook


@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_webhook()
    yield
    await shutdown_webhook()


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=False,
    allow_headers=["*"],
)

__all__ = [
    "app",
]
