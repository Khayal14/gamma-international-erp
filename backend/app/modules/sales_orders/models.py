from sqlalchemy import Column, String, Numeric, Text, Date, DateTime, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, SalesOrderStatus, PaymentType

class SalesOrder(UUIDBase, TimestampMixin):
    __tablename__ = "sales_orders"
    order_number = Column(String(30), nullable=False, index=True)
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    offer_id = Column(UUID(as_uuid=True), nullable=True)
    client_po_reference = Column(String(100), nullable=True)
    status = Column(SAEnum(SalesOrderStatus), nullable=False, default=SalesOrderStatus.CONFIRMED)
    sell_currency = Column(String(3), nullable=False, default="EGP")
    fx_rate_used = Column(Numeric(12, 6), nullable=True)
    subtotal = Column(Numeric(14, 2), nullable=False, default=0)
    vat_rate = Column(Numeric(5, 2), nullable=False, default=14)
    vat_amount = Column(Numeric(14, 2), nullable=False, default=0)
    total = Column(Numeric(14, 2), nullable=False, default=0)
    payment_type = Column(SAEnum(PaymentType), nullable=False, default=PaymentType.SINGLE)
    deposit_pct = Column(Numeric(5, 2), nullable=True)
    deposit_paid_at = Column(DateTime(timezone=True), nullable=True)
    final_pct = Column(Numeric(5, 2), nullable=True)
    final_paid_at = Column(DateTime(timezone=True), nullable=True)
    delivery_address = Column(JSONB, nullable=True)
    requested_delivery_date = Column(Date, nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=False)

class SalesOrderLine(UUIDBase):
    __tablename__ = "sales_order_lines"
    order_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_variant_id = Column(UUID(as_uuid=True), nullable=True)
    description_en = Column(Text, nullable=False)
    description_ar = Column(Text, nullable=True)
    quantity = Column(Numeric(14, 4), nullable=False)
    unit_price = Column(Numeric(12, 4), nullable=False)
    line_total = Column(Numeric(14, 2), nullable=False)
    source = Column(String(20), nullable=True)
