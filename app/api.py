from fastapi import FastAPI

from .db import database
from .db.database import engine
from .routers import category

database.Base.metadata.create_all(bind=engine)
app = FastAPI()

# app.include_router(clothes.router, prefix="/api/v1")
app.include_router(category.router, prefix="/api/v1")
