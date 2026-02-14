from fastapi import APIRouter

from .categories import router as categories_router
from .excercises import router as excercises_router
from .sets import router as sets_router
from .template_excercises import router as template_excercises_router
from .templates import router as templates_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(categories_router)
router.include_router(excercises_router)
router.include_router(sets_router)
router.include_router(template_excercises_router)
router.include_router(templates_router)


__all__ = [
    "router",
]
