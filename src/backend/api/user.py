from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from crud.user import UserCRUD
from crud.dependencies import get_user_crud
import schemas.user as user_schema

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=List[user_schema.Base])
async def get_users(db: UserCRUD = Depends(get_user_crud)):
    return await db.get_users()


@router.post("")
async def register(
    new_user: user_schema.Register, db: UserCRUD = Depends(get_user_crud)
):
    db_user = await db.get_user_by_username(username=new_user.username)
    if db_user:
        raise HTTPException(status_code=409, detail="Username already registered")
    await db.create_user(new_user)
    return status.HTTP_201_CREATED

@router.get("/{user_id}", response_model=user_schema.Base)
async def get_user(user_id: int, db: UserCRUD = Depends(get_user_crud)):
    user = await db.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user