from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/clothes")


@router.get("/")
async def read_items():
    return []


@router.get("/{cloth_id}")
async def read_item(item_id: str):
    return {}


@router.put("/{item_id}")
async def update_item(item_id: str):
    return {}
