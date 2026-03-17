from sqlalchemy import Column, String, Boolean, Text, Numeric, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, ClientType

class Client(UUIDBase, TimestampMixin):
    __tablename__ = "clients"
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    name_en = Column(String(255), nullable=False)
    name_ar = Column(String(255), nullable=True)
    client_type = Column(SAEnum(ClientType), nullable=False, default=ClientType.BUSINESS)
    email = Column(String(255), nullable=True)
    phone = Column(String(30), nullable=True)
    country = Column(String(100), nullable=True)
    billing_address = Column(JSONB, nullable=True)
    vat_registered = Column(Boolean, nullable=False, default=False)
    vat_number = Column(String(50), nullable=True)
    preferred_currency = Column(String(3), nullable=False, default="EGP")
    payment_terms_days = Column(Numeric, nullable=False, default=30)
    credit_limit = Column(Numeric(14, 2), nullable=True)
    assigned_sales_rep = Column(UUID(as_uuid=True), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    notes = Column(Text, nullable=True)
