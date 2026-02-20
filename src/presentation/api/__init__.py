from .app import app

from .routers import router

app.include_router(router)
