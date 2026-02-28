from aiogram import Router

from .add_set import router as add_set_router

router = Router()

router.include_router(add_set_router)


__all__ = [
    "router",
]
