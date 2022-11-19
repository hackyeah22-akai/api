import shutil

from fastapi import FastAPI, File, UploadFile
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


@app.post("/files/")
async def create_file(file: bytes | None = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(image: UploadFile | None = None):
    if not image:
        return {"message": "No upload file sent"}
    else:
        with open(image.filename, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        return {"filename": image.filename}


app.include_router(clothes_router.router, prefix="/api/v1")
app.include_router(categories_router.router, prefix="/api/v1")
