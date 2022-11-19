from fastapi import APIRouter

from ..db import crud, get_db, schemas

router = APIRouter(prefix="/clothes")


@router.post("/category", response_model=schemas.Category)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):  # uwaga typ Session nie SessionLocal
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, category=user)


@router.get("/{cloth_id}")
async def read_item(item_id: str):
    return {}


@router.put("/{item_id}")
async def update_item(item_id: str):
    return {}
