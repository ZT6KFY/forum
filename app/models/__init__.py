# app/models/__init__.py
from .admin_logs.admin_logs import AdminLogs
from .posts.posts import Posts
from .boards.boards import Boards
from .boards.board_categories import BoardCategories
from .post_votes.post_votes import PostVotes
from .threads.threads import Threads
from .users.users import Users

__all__ = [
    "AdminLogs",
    "Posts",
    "Boards",
    "BoardCategories",
    "PostVotes",
    "Threads",
    "Users",
]
