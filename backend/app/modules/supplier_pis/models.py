from sqlalchemy import Column, String, Integer, Numeric, Text, Date, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category

class SupplierPI(UUIDBase, TimestampMixin):
    __tablename__ = "supplier_pis"
    pi_number = Column(String(50), nullable=True)
    supplier_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    lead_id = Column(UUID(as_uuid=True), nullable=True)
    currency = Column(String(3), nullable=False, default="USD")
    fx_rate_snapshot = Column(Numeric(12, 6), nullable=True)
    subtotal_foreign = Column(Numeric(14, 4), nullable=False, default=0)
    shipping_cost_foreign = Column(Numeric(14, 4), nullable=True)
    valid_until = Column(Date, nullable=True)
    received_date = Column(Date, nullable=True)
    attachment_url = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

class SupplierPILine(UUIDBase):
    __tablename__ = "supplier_pi_lines"
    pi_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_variant_id = Column(UUID(as_uuid=True), nullable=True)
    description = Column(Text, nullable=False)
    quantity = Column(Numeric(14, 4), nullable=False)
    unit_price_foreign = Column(Numeric(12, 4), nullable=False)
    line_total_foreign = Column(Numeric(14, 4), nullable=False)
    sort_order = Column(Integer, nullable=False, default=0)
