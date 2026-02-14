from fastapi import APIRouter


from .list import router as list_router

router = APIRouter(
    prefix="/categories",
    tags=["Категории"],
)


router.include_router(list_router)


__all__ = [
    "router",
]
