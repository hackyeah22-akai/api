from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    savings: str
    max_items: int


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
