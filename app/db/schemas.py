import datetime

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    savings: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class ClothBase(BaseModel):
    name: str
    photo: str


class ClothCreate(ClothBase):
    category_id: int


class Cloth(ClothBase):
    id: int
    user: str
    category: Category

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
