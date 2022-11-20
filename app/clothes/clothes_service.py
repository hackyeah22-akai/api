import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import clothes_models, clothes_schemas
from .utilities import is_used


def get_user_id(authorization: str) -> str:
    if authorization.startswith("Bearer "):
        authorization = authorization.replace("Bearer ", "", 1)
    return authorization


def get_clothes(db: Session, authorization: str):
    user = get_user_id(authorization)
    return db.query(clothes_models.Cloth) \
        .filter(clothes_models.Cloth.user == user) \
        .filter(clothes_models.Cloth.status == "available") \
        .all()


def get_cloth(cloth_id: int, db: Session, authorization: str):
    user = get_user_id(authorization)
    return db.query(clothes_models.Cloth) \
        .filter(clothes_models.Cloth.id == cloth_id) \
        .filter(clothes_models.Cloth.user == user) \
        .filter(clothes_models.Cloth.status == "available") \
        .first()


def create_cloth(db: Session, cloth: clothes_schemas.ClothCreate, authorization: str):
    user = get_user_id(authorization)
    db_cloth = clothes_models.Cloth(**cloth.dict(),
                                    user=user,
                                    status="available",
                                    created_at=datetime.date.today())
    db.add(db_cloth)
    db.commit()
    db.refresh(db_cloth)
    max_items = db_cloth.category.max_items
    items_in_category = db.query(clothes_models.Cloth).filter(
        clothes_models.Cloth.category_id == cloth.category_id).filter(
        clothes_models.Cloth.user == user).all()
    return len(items_in_category) > max_items


def add_use(db: Session, use: clothes_schemas.UseCreate):
    db_use = clothes_models.Use(**use.dict())
    db.add(db_use)
    db.commit()
    db.refresh(db_use)
    db_use.cloth.last_used = db_use.date
    db.add(db_use.cloth)
    db.commit()


def delete_cloth(db: Session, cloth_id: int, authorization: str, status: str):
    user = get_user_id(authorization)
    cloth = db.query(clothes_models.Cloth) \
        .filter(clothes_models.Cloth.id == cloth_id) \
        .filter(clothes_models.Cloth.user == user) \
        .first()
    if not cloth:
        raise HTTPException(status_code=404, detail="Cloth not found!")
    cloth.status = status
    db.add(cloth)
    db.commit()


def get_unused_clothes(db: Session, authorization: str):
    unused_clothes = []
    clothes = get_clothes(db, authorization)
    for cloth in clothes:
        seasons = []
        if cloth.is_spring:
            seasons.append(0)
        if cloth.is_summer:
            seasons.append(1)
        if cloth.is_autumn:
            seasons.append(2)
        if cloth.is_winter:
            seasons.append(3)
        if not is_used(cloth.last_used if cloth.last_used is not None else cloth.created_at, seasons):
            unused_clothes.append(cloth)
    return unused_clothes


def get_unavailable_clothes(db: Session, authorization: str):
    user = get_user_id(authorization)
    return db.query(clothes_models.Cloth) \
        .filter(clothes_models.Cloth.user == user) \
        .filter(clothes_models.Cloth.status != "available") \
        .all()
