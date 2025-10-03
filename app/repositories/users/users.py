from app.models import Users
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    UserCreate,
    UserUpdate,
)


class UserRepository(BaseRepository[Users, UserCreate, UserUpdate]):
    pass


user_repository = UserRepository(Users)
