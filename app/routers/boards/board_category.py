from typing import List
from uuid import UUID

from fastapi import APIRouter, Path, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import repositories
from app.core.deps.deps import get_db
from app import schemas

router = APIRouter()


@router.get("", response_model=List[schemas.BoardCategoryInfo])
async def get_board_categories(db: AsyncSession = Depends(get_db)):
    """Получить список всех категорий досок"""
    res = await repositories.board_category_repository.get_all(db)
    return res


@router.get("/{category_sid}", response_model=schemas.BoardCategoryInfo)
async def get_board_category_by_sid(
    category_sid: UUID = Path(..., description="UUID категории доски"),
    db: AsyncSession = Depends(get_db),
):
    """Получить информацию о категории доски по её UUID"""
    category = await repositories.board_category_repository.get_by_sid(
        db, sid=category_sid
    )
    if not category:
        raise HTTPException(status_code=404, detail="Board category not found")
    return category
