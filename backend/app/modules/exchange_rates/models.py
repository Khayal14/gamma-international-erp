from sqlalchemy import Column, String, Numeric, Date
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin

class ExchangeRate(UUIDBase, TimestampMixin):
    __tablename__ = "exchange_rates"
    from_currency = Column(String(3), nullable=False)
    to_currency = Column(String(3), nullable=False)
    rate = Column(Numeric(12, 6), nullable=False)
    effective_date = Column(Date, nullable=False, index=True)
    created_by = Column(UUID(as_uuid=True), nullable=True)
