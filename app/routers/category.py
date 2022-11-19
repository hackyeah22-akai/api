from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud, get_db, schemas
from ..db.database import SessionLocal

router = APIRouter(prefix="/category")

@router.post("", response_model=schemas.Category)
async def create_user(category: schemas.CategoryCreate,
                db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.get("/{category_id}")
async def read_item(item_id: str):
    return {}


@router.put("/{item_id}")
async def update_item(item_id: str):
    return {}
