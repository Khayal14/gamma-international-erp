from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.deps import get_current_user, require_roles
from app.modules.auth.service import AuthService
from app.modules.auth.schemas import (
    LoginRequest, TokenResponse, RefreshRequest,
    UserCreate, UserUpdate, UserResponse
)
from app.shared.enums import UserRole
from typing import Annotated, List

router = APIRouter(prefix="/auth", tags=["Auth"])
users_router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, db: Annotated[AsyncSession, Depends(get_db)]):
    return await AuthService(db).login(data)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(data: RefreshRequest, db: Annotated[AsyncSession, Depends(get_db)]):
    return await AuthService(db).refresh(data.refresh_token)


@users_router.post("", response_model=UserResponse,
                   dependencies=[Depends(require_roles(UserRole.ADMIN))])
async def create_user(
    data: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]
):
    return await AuthService(db).create_user(data)


@users_router.get("/me", response_model=UserResponse)
async def get_me(current_user=Depends(get_current_user)):
    return current_user
