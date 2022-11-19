from fastapi import FastAPI
from sqlalchemy import Column, String
from sqlalchemy.orm import Session

from .categories import categories_router
from .clothes import clothes_router
from .config import *


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, unique=True, index=True)


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    with Session(engine) as db:
        db.query(User).filter(User.email == "test@test.com").first()
        if User is not None:
            return
        user = User(email="test@test.com")
        db.add(user)
        db.commit()


app.include_router(clothes_router.router, prefix="/api/v1")
app.include_router(categories_router.router, prefix="/api/v1")
