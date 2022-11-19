from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    savings: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int


class ClothBase(BaseModel):
    category_id: int
    name: str


class ClothCreate(ClothBase):
    pass


class Cloth(ClothBase):
    id: int
    user_id: int
    category: Category

    class Config:
        orm_mode = True