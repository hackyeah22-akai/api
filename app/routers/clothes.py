from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import crud, get_db, schemas

router = APIRouter(prefix="/clothes")


@router.post("", response_model=schemas.Cloth)
async def create_cloth(cloth: schemas.ClothCreate,
                       db: Session = Depends(get_db)):
    return crud.create_cloth(db, cloth)


@router.get("", response_model=list[schemas.Cloth])
async def read_clothes(db: Session = Depends(get_db)):
    return crud.get_clothes(db)


@router.get("/{cloth_id}", response_model=schemas.Cloth)
async def read_cloth(cloth_id: int, db: Session = Depends(get_db)):
    return crud.get_cloth(cloth_id, db)
