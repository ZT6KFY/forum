from app.models import Threads
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    ThreadCreate,
    ThreadUpdate,
)


class ThreadRepository(BaseRepository[Threads, ThreadCreate, ThreadUpdate]):
    pass


thread_repository = ThreadRepository(Threads)
