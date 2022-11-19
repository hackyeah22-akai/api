from config import *
from fastapi import FastAPI

from .categories import categories_router
from .clothes import clothes_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(clothes_router.router, prefix="/api/v1")
app.include_router(categories_router.router, prefix="/api/v1")
