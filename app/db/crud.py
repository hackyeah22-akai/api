from sqlalchemy.orm import Session

from . import models, schemas


def get_cloths(db: Session):
    return db.query(models.Cloth)


def create_cloth(db: Session, cloth: schemas.ClothCreate):
    db_cloth = models.Cloth(**cloth.dict(), user_id=1)
    db.add(db_cloth)
    db.commit()
    db.refresh(db_cloth)
    return db_cloth


def get_categories(db: Session):
    return db.query(models.Category)


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
