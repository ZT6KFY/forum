from fastapi import APIRouter

from .users import users, auth
from .boards import boards, board_category
from .posts import posts, post_votes
from .threads import threads, thread_votes
from .admin_logs import admin_logs

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router, tags=["Users"], prefix="/users")
api_router.include_router(auth.router, tags=["Auth"], prefix="/auth")
api_router.include_router(boards.router, tags=["Boards"], prefix="/boards")
api_router.include_router(
    board_category.router, tags=["Board category"], prefix="/board_category"
)
api_router.include_router(post_votes.router, tags=["PostVotes"], prefix="/post_votes")
api_router.include_router(posts.router, tags=["Posts"], prefix="/posts")
api_router.include_router(threads.router, tags=["Threads"], prefix="/threads")
api_router.include_router(
    thread_votes.router, tags=["ThreadVotes"], prefix="/thread_votes"
)
api_router.include_router(admin_logs.router, tags=["AdminLogs"], prefix="/admin_logs")
