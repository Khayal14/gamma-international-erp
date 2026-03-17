from sqlalchemy import Column, String, Boolean, DateTime, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import UserRole, Language, Theme


class User(UUIDBase, TimestampMixin):
    __tablename__ = "users"

    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(SAEnum(UserRole), nullable=False, default=UserRole.SALES_REP)
    branch_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=False, default=list)
    default_language = Column(SAEnum(Language), nullable=False, default=Language.EN)
    theme = Column(SAEnum(Theme), nullable=False, default=Theme.LIGHT)
    is_active = Column(Boolean, nullable=False, default=True)
    last_login_at = Column(DateTime(timezone=True), nullable=True)
