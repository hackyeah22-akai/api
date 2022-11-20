from sqlalchemy.orm import Session

from . import users_models, users_schemas


def create_user(db: Session, user: users_schemas.UserBase):
    db_user = users_models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
