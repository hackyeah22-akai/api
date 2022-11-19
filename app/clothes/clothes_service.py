import datetime

from sqlalchemy.orm import Session

from . import clothes_models, clothes_schemas


def get_clothes(db: Session):
    return db.query(clothes_models.Cloth).all()


def get_cloth(cloth_id: int, db: Session):
    return db.query(clothes_models.Cloth).filter(clothes_models.Cloth.id == cloth_id).first()


def create_cloth(db: Session, cloth: clothes_schemas.ClothCreate):
    db_cloth = clothes_models.Cloth(**cloth.dict(), user="test@test.com", created_at=datetime.date.today())
    db.add(db_cloth)
    db.commit()
    db.refresh(db_cloth)
    return db_cloth


def add_use(db: Session, use: clothes_schemas.UseCreate):
    db_use = clothes_models.Use(**use.dict())
    db.add(db_use)
    db.commit()
    db.refresh(db_use)
    return db_use
