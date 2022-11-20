from sqlalchemy import Column, String

from app.config import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, unique=True, index=True)
