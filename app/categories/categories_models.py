from sqlalchemy import Column, Integer, String

from app.config import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_items = Column(Integer, nullable=False)
    savings = Column(String, nullable=False)
