from fastapi import APIRouter

from .auth import router as auth_router
from .categories import router as categories_router
from .exercises import router as excercises_router
from .sets import router as sets_router
from .template_exercises import router as template_exercises_router
from .templates import router as templates_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(auth_router)
router.include_router(categories_router)
router.include_router(excercises_router)
router.include_router(sets_router)
router.include_router(template_exercises_router)
router.include_router(templates_router)


__all__ = [
    "router",
]
