from typing import List
from uuid import UUID

from fastapi import APIRouter, Path, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import repositories
from app.core.deps.deps import get_db
from app import schemas

router = APIRouter()


@router.get("", response_model=List[schemas.BoardInfo])
async def get_boards(db: AsyncSession = Depends(get_db)):
    res = await repositories.board_repository.get_all(db)
    return res


@router.get(
    "/category/{board_category_sid}",
    response_model=List[schemas.BoardInfo],
    summary="Get Boards By Category",
)
async def get_boards_by_category(
    db: AsyncSession = Depends(get_db),
    board_category_sid: UUID = Path(...),
):
    res = await repositories.board_repository.get_by_board_category(
        db, board_category_sid
    )
    return res


@router.get("/{board_sid}", response_model=schemas.BoardInfo)
async def get_board_by_sid(
    board_sid: UUID = Path(..., description="UUID of the board"),
    db: AsyncSession = Depends(get_db),
):
    board = await repositories.board_repository.get_by_sid(db, sid=board_sid)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return board


@router.post("", response_model=schemas.BoardInfo)
async def create_board(
    post_data: schemas.BoardCreate, db: AsyncSession = Depends(get_db)
):
    board_category = await repositories.board_category_repository.get_by_sid(
        db, sid=post_data.board_category_sid
    )

    if not board_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Сущность: категория доски не найдена",
        )

    return await repositories.board_repository.create(db, post_data)
