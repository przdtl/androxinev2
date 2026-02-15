from fastapi import APIRouter

from .telegram import router as telegram_router

router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация"],
)

router.include_router(telegram_router)
