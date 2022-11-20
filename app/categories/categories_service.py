from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import categories_models, categories_schemas


def get_categories(db: Session):
    return db.query(categories_models.Category).all()


def get_category(category_id: int, db: Session):
    category = db.query(categories_models.Category) \
                 .filter(categories_models.Category.id == category_id) \
                 .first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found!")
    return category


def create_category(db: Session, category: categories_schemas.CategoryCreate):
    db_category = categories_models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
