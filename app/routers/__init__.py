from fastapi import APIRouter

from .users import users  # admin_lgos, boards, post_votes, posts, threads
from .boards import boards
from .post_votes import post_votes
from .posts import posts
from .threads import threads
from .admin_logs import admin_logs
from .boards import board_category

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router, tags=["Users"], prefix="/users")
api_router.include_router(boards.router, tags=["Boards"], prefix="/boards")
api_router.include_router(
    board_category.router, tags=["Board category"], prefix="/board_category"
)
api_router.include_router(post_votes.router, tags=["PostVotes"], prefix="/post_votes")
api_router.include_router(posts.router, tags=["Posts"], prefix="/posts")
api_router.include_router(threads.router, tags=["Threads"], prefix="/threads")
api_router.include_router(admin_logs.router, tags=["AdminLogs"], prefix="/admin_logs")
