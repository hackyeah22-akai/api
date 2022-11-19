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


class ClothCreate(ClothBase):
    category_id: int
    pass


class Cloth(ClothBase):
    id: int
    user: str
    category: Category

    class Config:
        orm_mode = True
