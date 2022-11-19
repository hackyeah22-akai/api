from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import get_db

from . import categories_schemas, categories_service

router = APIRouter(prefix="/category")

TAGS = ['Categories']

@router.post("",
             response_model=categories_schemas.Category,
             tags=TAGS)
async def create_category(category: categories_schemas.CategoryCreate,
                          database: Session = Depends(get_db)):
    return categories_service.create_category(database, category)


@router.get("",
            response_model=list[categories_schemas.Category],
            tags=TAGS)
async def read_categories(database: Session = Depends(get_db)):
    return categories_service.get_categories(database)


@router.get("/{category_id}",
            response_model=categories_schemas.Category,
            tags=TAGS)
async def read_category(category_id: int,
                        database: Session = Depends(get_db)):
    return categories_service.get_category(category_id, database)
