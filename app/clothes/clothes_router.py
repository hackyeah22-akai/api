from botocore.client import BaseClient
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.config import get_db

from ..config import s3_auth
from ..s3.upload import upload_file_to_bucket
from . import clothes_schemas, clothes_service

router = APIRouter(prefix="/clothes")

TAGS = ['Clothes']


@router.post("", tags=TAGS)
async def create_cloth(cloth: clothes_schemas.ClothCreate,
                       db: Session = Depends(get_db)):
    return {"too_much": clothes_service.create_cloth(db, cloth)}


@router.delete("/{cloth_id}",
               tags=TAGS)
async def delete_cloth(cloth_id: int, db: Session = Depends(get_db)):
    return clothes_service.delete_cloth(db, cloth_id)


@router.get("",
            response_model=list[clothes_schemas.Cloth],
            tags=TAGS)
async def read_clothes(db: Session = Depends(get_db)):
    return clothes_service.get_clothes(db)


@router.get("/unused",
            response_model=list,
            tags=TAGS)
async def get_unused_clothes(db: Session = Depends(get_db)):
    return clothes_service.get_unused_clothes(db)


@router.get("/{cloth_id}",
            response_model=clothes_schemas.Cloth,
            tags=TAGS)
async def read_cloth(cloth_id: int, db: Session = Depends(get_db)):
    return clothes_service.get_cloth(cloth_id, db)


@router.post("/use/{cloth_id}",
             tags=TAGS,
             status_code=status.HTTP_201_CREATED)
async def add_cloth_use(cloth_id: int, db: Session = Depends(get_db)):
    use = clothes_schemas.UseCreate(cloth_id=cloth_id)
    clothes_service.add_use(db, use)


@router.post("/images", status_code=status.HTTP_201_CREATED, tags=TAGS)
async def upload_file(s3: BaseClient = Depends(s3_auth),
                      file_obj: UploadFile = File(...)):
    upload_obj = upload_file_to_bucket(s3_client=s3,
                                       file_obj=file_obj.file,
                                       object_name=file_obj.filename)

    if upload_obj != '':
        return JSONResponse(content={'url': upload_obj},
                            status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="File could not be uploaded")
