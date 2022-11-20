import datetime

from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from . import clothes_models, clothes_schemas
from .utilities import is_used


def get_clothes(db: Session):
    return db.query(clothes_models.Cloth).all()


def get_cloth(cloth_id: int, db: Session):
    return db.query(clothes_models.Cloth) \
             .filter(clothes_models.Cloth.id == cloth_id) \
             .first()


def create_cloth(db: Session, cloth: clothes_schemas.ClothCreate):
    db_cloth = clothes_models.Cloth(**cloth.dict(),
                                    user="test@test.com",
                                    created_at=datetime.date.today())
    db.add(db_cloth)
    db.commit()
    db.refresh(db_cloth)
    max_items = db_cloth.category.max_items
    items_in_category = db.query(clothes_models.Cloth).filter(
        clothes_models.Cloth.category_id == cloth.category_id).all()
    return len(items_in_category) > max_items


def add_use(db: Session, use: clothes_schemas.UseCreate):
    db_use = clothes_models.Use(**use.dict())
    db.add(db_use)
    db.commit()
    db.refresh(db_use)
    return db_use


def delete_cloth(db: Session, cloth_id: int):
    cloth = db.query(clothes_models.Cloth) \
              .filter(clothes_models.Cloth.id == cloth_id) \
              .first()
    if not cloth:
        raise HTTPException(status_code=404, detail="Cloth not found!")
    db.delete(cloth)
    db.commit()
    # TODO: Return how much resourses you did save,
    return {}


def get_unused_clothes(db: Session):
    sql = text(
        """select c.id, coalesce(u.date, c.created_at) as last_used, c.is_spring, c.is_summer, c.is_autumn, c.is_winter from clothes c left join uses u on c.id = u.cloth_id""")
    cloth_ids = []
    result = db.execute(sql)
    for row in result:
        cloth_id = row.id
        last_used = row.last_used
        seasons = []
        if row.is_spring:
            seasons.append(0)
        if row.is_summer:
            seasons.append(1)
        if row.is_autumn:
            seasons.append(2)
        if row.is_winter:
            seasons.append(3)
        if is_used(last_used, seasons):
            cloth_ids.append(cloth_id)
    return db.query(clothes_models.Cloth) \
             .filter(~clothes_models.Cloth.id.in_(cloth_ids)) \
             .all()
