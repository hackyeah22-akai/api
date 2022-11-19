from sqlalchemy.orm import Session

from . import models, schemas


def get_categories(db: Session):
    return db.query(models.Category).all()


def get_category(category_id: int, db: Session):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
