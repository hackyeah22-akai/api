from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..db.dbconnector import get_db

router = APIRouter(prefix="/category")


@router.post("", response_model=schemas.Category)
async def create_category(category: schemas.CategoryCreate,
                          database: Session = Depends(get_db)):
    return crud.create_category(database, category)


@router.get("", response_model=list[schemas.Category])
async def read_categories(database: Session = Depends(get_db)):
    return crud.get_categories(database)


@router.get("/{category_id}", response_model=schemas.Category)
async def read_category(category_id: int,
                        database: Session = Depends(get_db)):
    return crud.get_category(category_id, database)
