from fastapi import APIRouter, Depends, Response, Cookie, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps.deps import get_db
from app.services.auth_service import auth_service
from app.schemas.auth.auth import UserRegister, UserLogin
from app.schemas.auth.token import Token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=Token)
async def register(
    user_in: UserRegister, response: Response, db: AsyncSession = Depends(get_db)
):
    token_data = await auth_service.register_user(db, user_in)

    response.set_cookie(
        key="refresh_token",
        value=token_data.refresh_token,
        httponly=True,
        samesite="lax",
        secure=False,
    )
    return token_data


@router.post("/login", response_model=Token)
async def login(
    user_in: UserLogin, response: Response, db: AsyncSession = Depends(get_db)
):
    token_data = await auth_service.authenticate_user(db, user_in)

    response.set_cookie(
        key="refresh_token",
        value=token_data.refresh_token,
        httponly=True,
        samesite="lax",
        secure=False,
    )
    return token_data


@router.post("/logout")
async def logout(
    response: Response,
    refresh_token: str = Cookie(None),
):
    if not refresh_token:
        return {"msg": "Successfully logged out"}

    await auth_service.logout(refresh_token)

    response.delete_cookie(key="refresh_token")
    return {"msg": "Successfully logged out"}


@router.post("/refresh", response_model=Token)
async def refresh_token(
    response: Response,
    refresh_token: str = Cookie(None),
    db: AsyncSession = Depends(get_db),
):
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token missing"
        )

    new_tokens = await auth_service.refresh_token(db, refresh_token)

    response.set_cookie(
        key="refresh_token",
        value=new_tokens.refresh_token,
        httponly=True,
        samesite="lax",
        secure=False,
    )
    return new_tokens
