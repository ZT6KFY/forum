from typing import List
from uuid import UUID

from fastapi import APIRouter, Path, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import repositories
from app.core.deps.deps import get_db
from app import schemas

router = APIRouter()


@router.get("", response_model=List[schemas.PostInfo])
async def get_posts(db: AsyncSession = Depends(get_db)):
    res = await repositories.post_repository.get_all(db)
    return res


@router.get("/{post_sid}", response_model=schemas.PostInfo)
async def get_post_by_sid(
    post_sid: UUID = Path(..., description="UUID of the post"),
    db: AsyncSession = Depends(get_db),
):
    post = await repositories.post_repository.get_by_sid(db, sid=post_sid)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
