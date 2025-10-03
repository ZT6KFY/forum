from typing import List
from uuid import UUID

from fastapi import APIRouter, Path, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import repositories
from app.core.deps.deps import get_db
from app import schemas

router = APIRouter()


@router.get("", response_model=List[schemas.UserInfo])
async def get_users(db: AsyncSession = Depends(get_db)):
    res = await repositories.user_repository.get_users(db)
    return res


@router.get("/{user_sid}", response_model=schemas.UserInfo)
async def get_user_by_sid(user_sid: UUID = Path(), db: AsyncSession = Depends(get_db)):
    user = repositories.user_repository.get_by_sid(db, sid=user_sid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/{user_sid}/threads")
async def get_user_threads(user_sid: UUID = Path(), db: AsyncSession = Depends(get_db)):
    pass
