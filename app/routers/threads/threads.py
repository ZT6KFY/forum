from typing import List
from uuid import UUID

from fastapi import APIRouter, Path, HTTPException, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app import repositories, schemas
from app.core.deps.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.ThreadInfo])
async def get_threads(db: AsyncSession = Depends(get_db)):
    res = await repositories.thread_repository.get_all(db)
    return res


@router.get("/{thread_sid}", response_model=schemas.ThreadInfo)
async def get_thread_by_sid(
    thread_sid: UUID = Path(..., description="UUID of the thread"),
    db: AsyncSession = Depends(get_db),
):
    thread = await repositories.thread_repository.get_by_sid(db, sid=thread_sid)
    if not thread:
        raise HTTPException(status_code=404, detail="Thread not found")
    return thread


@router.post("", response_model=schemas.ThreadInfo)
async def create_thread(
    post_data: schemas.ThreadCreate, db: AsyncSession = Depends(get_db)
):
    return await repositories.thread_repository.create(db, post_data)


@router.put("/{thread_sid}", response_model=schemas.ThreadInfo)
async def update_thread(
    thread_sid: UUID = Path(...),
    thread_data: schemas.ThreadUpdate = Body(...),
    db: AsyncSession = Depends(get_db),
):
    thread = await repositories.thread_repository.get_by_sid(db, sid=thread_sid)
    if not thread:
        raise HTTPException(status_code=404, detail="Thread not found")

    return await repositories.thread_repository.update(
        db, db_obj=thread, schema=thread_data
    )
