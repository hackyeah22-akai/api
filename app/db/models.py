from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, unique=True, index=True)
    clothes = relationship("Cloth")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    savings = Column(String, nullable=False)


class Cloth(Base):
    __tablename__ = "clothes"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("users.email"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    category = relationship("Category")


class Use(Base):
    __tablename__ = "uses"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    cloth_id = Column(Integer, ForeignKey("clothes.id"), nullable=False)
    cloth = relationship("Cloth")
