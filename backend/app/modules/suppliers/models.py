from sqlalchemy import Column, String, Boolean, Integer, Text, Enum as SAEnum
from sqlalchemy.dialects.postgresql import ARRAY
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import SupplierType, Category

class Supplier(UUIDBase, TimestampMixin):
    __tablename__ = "suppliers"
    name = Column(String(255), nullable=False)
    country = Column(String(100), nullable=True)
    supplier_type = Column(SAEnum(SupplierType), nullable=False, default=SupplierType.FOREIGN)
    email = Column(String(255), nullable=True)
    phone = Column(String(30), nullable=True)
    preferred_currency = Column(String(3), nullable=False, default="USD")
    payment_terms = Column(Text, nullable=True)
    lead_time_days = Column(Integer, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    notes = Column(Text, nullable=True)
