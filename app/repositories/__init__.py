from .users.users import (
    user_repository as user_repository,
)

from .boards.boards import (
    board_repository as board_repository,
)

from app.repositories.posts.post_votes import (
    post_votes_repository as post_votes_repository,
)

from .posts.posts import (
    post_repository as post_repository,
)

from .threads.threads import (
    thread_repository as thread_repository,
)

from .threads.thread_votes import (
    thread_votes_repository as thread_votes_repository,
)

from .admin_logs.admin_logs import (
    admin_log_repository as admin_log_repository,
)

from .boards.board_categories import (
    board_category_repository as board_category_repository,
)
