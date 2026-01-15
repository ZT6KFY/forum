from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.deps.deps import get_db
from app.services.auth_service import auth_service
from app.schemas.auth.auth import UserRegister, UserLogin
from app.schemas.auth.token import Token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=Token)
async def register(user_in: UserRegister, db: AsyncSession = Depends(get_db)):
    return await auth_service.register_user(db, user_in)


@router.post("/login", response_model=Token)
async def login(user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    return await auth_service.authenticate_user(db, user_in)
