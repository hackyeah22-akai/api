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
    category_id: int
    name: str


class ClothCreate(ClothBase):
    pass


class Cloth(ClothBase):
    id: int
    user: str
    category: Category

    class Config:
        orm_mode = True
