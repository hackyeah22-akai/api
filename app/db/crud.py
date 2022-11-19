from sqlalchemy.orm import Session

from . import models, schemas


def get_clothes(db: Session):
    return db.query(models.Cloth).all()


def get_cloth(cloth_id: int, db: Session):
    return db.query(models.Cloth).filter(models.Cloth.id == cloth_id).first()


def create_cloth(db: Session, cloth: schemas.ClothCreate):
    db_cloth = models.Cloth(**cloth.dict(), user="test@test.com")
    db.add(db_cloth)
    db.commit()
    db.refresh(db_cloth)
    return db_cloth


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
