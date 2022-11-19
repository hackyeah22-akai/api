from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud, get_db, schemas

router = APIRouter(prefix="/category")


@router.post("", response_model=schemas.Category)
async def create_category(category: schemas.CategoryCreate,
                          db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.get("", response_model=list[schemas.Category])
async def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=schemas.Category)
async def read_category(category_id: int, db: Session = Depends(get_db)):
    return crud.get_category(category_id, db)
