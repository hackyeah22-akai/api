from fastapi import FastAPI

from .db import Base, engine
from .routers import category

Base.metadata.create_all(bind=engine)
app = FastAPI()

# app.include_router(clothes.router, prefix="/api/v1")
app.include_router(category.router, prefix="/api/v1")
