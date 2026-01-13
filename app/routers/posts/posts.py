from typing import List
from uuid import UUID

from fastapi import APIRouter, Path, HTTPException, Depends, Body, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import repositories, schemas
from app.core.deps.deps import get_db
from app.schemas.posts.post_votes import PostVotesCreate, VoteResponse
from app.repositories.posts.post_votes import post_votes_repository

router = APIRouter()


@router.get("", response_model=List[schemas.PostInfo])
async def get_posts(db: AsyncSession = Depends(get_db)):
    res = await repositories.post_repository.get_all(db)
    return res


@router.get("/by-thread/{thread_sid}", response_model=List[schemas.PostInfo])
async def get_posts_by_thread(
    db: AsyncSession = Depends(get_db),
    thread_sid: UUID = Path(...),
):
    res = await repositories.post_repository.get_by_thread(db, thread_sid)
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


@router.post("", response_model=schemas.PostInfo)
async def create_post(
    post_data: schemas.PostCreate, db: AsyncSession = Depends(get_db)
):
    thread = await repositories.thread_repository.get_by_sid(
        db, sid=post_data.thread_sid
    )

    if not thread:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="thread not found"
        )

    return await repositories.post_repository.create(db, post_data)


@router.put("/{post_sid}", response_model=schemas.PostInfo)
async def update_post(
    post_sid: UUID = Path(),
    post_data: schemas.PostUpdate = Body(...),
    db: AsyncSession = Depends(get_db),
):
    post = await repositories.post_repository.get_by_sid(db, sid=post_sid)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return await repositories.post_repository.update(db, db_obj=post, schema=post_data)


@router.post("/{post_sid}/vote", response_model=VoteResponse)
async def vote_post(
    post_sid: UUID,
    vote_in: PostVotesCreate,
    db: AsyncSession = Depends(get_db),
):
    new_score, current_vote = await post_votes_repository.toggle_vote(
        db=db, post_sid=post_sid, user_sid=vote_in.user_sid, value=vote_in.value
    )

    return VoteResponse(
        post_sid=post_sid, new_score=new_score, current_vote=current_vote
    )
