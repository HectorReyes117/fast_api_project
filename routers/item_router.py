from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.item_schema import ItemCreate, Item
import services.user_services as user_services
import services.item_services as item_services
from dependencies.get_db import get_db

router = APIRouter()


@router.post("/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
        user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    if user_services.get_user(db, user_id=user_id) is None:
        raise HTTPException(status_code=404, detail="User not found")
    return item_services.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_services.get_items(db, skip=skip, limit=limit)
    return items
