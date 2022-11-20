from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import get_db
from . import users_schemas, users_service

router = APIRouter(prefix="/user")

TAGS = ['Users']


@router.post("",
             response_model=users_schemas.UserBase,
             tags=TAGS)
async def create_user(user: users_schemas.UserBase,
                      database: Session = Depends(get_db)):
    return users_service.create_user(database, user)
