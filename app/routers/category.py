from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..db import schemas, crud
from ..db.database import SessionLocal

router = APIRouter(prefix="/category")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=schemas.Category)
def create_user(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.get("/{category_id}")
async def read_item(item_id: str):
    return {}


@router.put("/{item_id}")
async def update_item(item_id: str):
    return {}
