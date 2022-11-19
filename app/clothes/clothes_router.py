from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config import get_db
from . import clothes_service, clothes_schemas

router = APIRouter(prefix="/clothes")


@router.post("", response_model=clothes_schemas.Cloth)
async def create_cloth(cloth: clothes_schemas.ClothCreate,
                       db: Session = Depends(get_db)):
    return clothes_service.create_cloth(db, cloth)


@router.get("", response_model=list[clothes_schemas.Cloth])
async def read_clothes(db: Session = Depends(get_db)):
    return clothes_service.get_clothes(db)


@router.get("/{cloth_id}", response_model=clothes_schemas.Cloth)
async def read_cloth(cloth_id: int, db: Session = Depends(get_db)):
    return clothes_service.get_cloth(cloth_id, db)


@router.post("/use/{cloth_id}", status_code=status.HTTP_201_CREATED)
async def add_cloth_use(cloth_id: int, db: Session = Depends(get_db)):
    use = clothes_schemas.UseCreate(cloth_id=cloth_id)
    clothes_service.add_use(db, use)
