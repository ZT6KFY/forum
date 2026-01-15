import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.core.database.redis import redis_client
from app.repositories.users.users import user_repository
from app.utils.security import get_password_hash, verify_password, create_access_token
from app.schemas.auth.auth import UserRegister, UserLogin
from app.schemas.auth.token import Token


class AuthService:
    REDIS_PREFIX = "user"
    REFRESH_EXPIRE = 60 * 60 * 24 * 30

    async def register_user(self, db: AsyncSession, user_in: UserRegister) -> Token:
        if await user_repository.get_by_email(db, user_in.email):
            raise HTTPException(status_code=400, detail="Email already registered")

        if await user_repository.get_by_username(db, user_in.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken"
            )

        user_data = user_in.dict()
        hashed_pw = get_password_hash(user_data.pop("password"))
        user_data["password_hash"] = hashed_pw

        new_user = await user_repository.create(db, schema=user_data)

        return await self._create_tokens(new_user.sid)

    async def authenticate_user(self, db: AsyncSession, login_data: UserLogin) -> Token:
        user = await user_repository.get_by_email(db, login_data.email)
        if not user or not verify_password(login_data.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Incorrect email or password")

        return await self._create_tokens(user.sid)

    async def _create_tokens(self, user_sid: uuid.UUID) -> Token:
        access_token = create_access_token(user_sid)

        refresh_token = str(uuid.uuid4())

        await redis_client.set(
            f"{self.REDIS_PREFIX}:{user_sid}:refresh",
            refresh_token,
            ex=self.REFRESH_EXPIRE,
        )

        return Token(
            access_token=access_token, refresh_token=refresh_token, token_type="bearer"
        )


auth_service = AuthService()
