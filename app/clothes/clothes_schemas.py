import datetime

from pydantic import BaseModel

from ..categories.categories_schemas import Category


class ClothBase(BaseModel):
    name: str
    photo: str
    is_winter: bool = False
    is_spring: bool = False
    is_summer: bool = False
    is_autumn: bool = False


class ClothCreate(ClothBase):
    category_id: int


class Cloth(ClothBase):
    id: int
    user: str
    created_at: datetime.date
    category: Category
    last_used: datetime.date

    class Config:
        orm_mode = True


class UseBase(BaseModel):
    date: datetime.date = datetime.date.today()


class UseCreate(UseBase):
    cloth_id: int


class Use(UseBase):
    id: int

    class Config:
        orm_mode = True
