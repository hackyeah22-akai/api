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
