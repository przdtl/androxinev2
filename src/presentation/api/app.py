from contextlib import asynccontextmanager
import uuid

from fastapi import FastAPI
from fastapi import Request
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


@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


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
