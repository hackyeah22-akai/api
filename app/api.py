from fastapi import FastAPI

from .db import database
from .db.database import engine
from .routers import clothes

database.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(clothes.router, prefix="/api/v1")
