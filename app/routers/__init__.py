from fastapi import APIRouter

from .users import users  # admin_lgos, boards, post_votes, posts, threads

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router, tags=["Users"], prefix="/users")
