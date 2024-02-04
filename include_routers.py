from fastapi import FastAPI
from routers import user_router, item_router


def include_routers(app: FastAPI):
    app.include_router(user_router.router)
    app.include_router(item_router.router)