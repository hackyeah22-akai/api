from fastapi import FastAPI
from .routers import clothes

app = FastAPI()

app.include_router(clothes.router, prefix="/api/v1")
