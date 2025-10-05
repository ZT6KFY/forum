from fastapi import APIRouter

from .users import users  # admin_lgos, boards, post_votes, posts, threads
from .boards import boards
from .post_votes import post_votes

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router, tags=["Users"], prefix="/users")
api_router.include_router(boards.router, tags=["Boards"], prefix="/boards")
api_router.include_router(post_votes.router, tags=["PostVotes"], prefix="/post_votes")
# api_router.include_router(boards.router, tags=["Boards"], prefix="/boards")
# api_router.include_router(boards.router, tags=["Boards"], prefix="/boards")
# api_router.include_router(boards.router, tags=["Boards"], prefix="/boards")
