from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.config import Base


class Cloth(Base):
    __tablename__ = "clothes"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, ForeignKey("users.email"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)
    category = relationship("Category")


class Use(Base):
    __tablename__ = "uses"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    cloth_id = Column(Integer, ForeignKey("clothes.id"), nullable=False)
    cloth = relationship("Cloth")
