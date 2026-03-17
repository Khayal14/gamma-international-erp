from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.modules.auth.repository import UserRepository
from app.modules.auth.models import User
from app.modules.auth.schemas import LoginRequest, TokenResponse, UserCreate
from app.core.security import (
    hash_password, verify_password, create_access_token,
    create_refresh_token, decode_token
)
from app.core.exceptions import ConflictError
import jwt


class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def login(self, data: LoginRequest) -> TokenResponse:
        user = await self.repo.get_by_email(data.email)
        if not user or not verify_password(data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account disabled",
            )
        user.last_login_at = datetime.now(timezone.utc)
        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def refresh(self, refresh_token: str) -> TokenResponse:
        try:
            payload = decode_token(refresh_token)
            if payload.get("type") != "refresh":
                raise HTTPException(status_code=401, detail="Invalid token type")
            user = await self.repo.get_by_id(payload["sub"])
            if not user or not user.is_active:
                raise HTTPException(status_code=401, detail="User not found")
        except jwt.PyJWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def create_user(self, data: UserCreate) -> User:
        existing = await self.repo.get_by_email(data.email)
        if existing:
            raise ConflictError("A user with this email already exists")
        user = User(
            full_name=data.full_name,
            email=data.email,
            password_hash=hash_password(data.password),
            role=data.role,
            branch_ids=data.branch_ids,
            default_language=data.default_language,
            theme=data.theme,
        )
        return await self.repo.create(user)
