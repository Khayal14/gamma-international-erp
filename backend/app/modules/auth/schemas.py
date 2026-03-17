from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID
from app.shared.enums import UserRole, Language, Theme


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.SALES_REP
    branch_ids: List[UUID] = []
    default_language: Language = Language.EN
    theme: Theme = Theme.LIGHT


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    branch_ids: Optional[List[UUID]] = None
    default_language: Optional[Language] = None
    theme: Optional[Theme] = None
    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    id: UUID
    full_name: str
    email: str
    role: UserRole
    branch_ids: List[UUID]
    default_language: Language
    theme: Theme
    is_active: bool

    class Config:
        from_attributes = True
