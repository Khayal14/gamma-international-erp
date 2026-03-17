from sqlalchemy import Column, String, Numeric, Text, Date, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, SupplierPOStatus, PaymentType, PaymentStatus

class SupplierPO(UUIDBase, TimestampMixin):
    __tablename__ = "supplier_purchase_orders"
    po_number = Column(String(30), nullable=False, index=True)
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    supplier_id = Column(UUID(as_uuid=True), nullable=False)
    sales_order_id = Column(UUID(as_uuid=True), nullable=True)
    supplier_pi_id = Column(UUID(as_uuid=True), nullable=True)
    status = Column(SAEnum(SupplierPOStatus), nullable=False, default=SupplierPOStatus.DRAFT)
    currency = Column(String(3), nullable=False, default="USD")
    fx_rate_at_order = Column(Numeric(12, 6), nullable=True)
    subtotal_foreign = Column(Numeric(14, 4), nullable=False, default=0)
    shipping_cost_foreign = Column(Numeric(14, 4), nullable=True)
    total_foreign = Column(Numeric(14, 4), nullable=False, default=0)
    payment_type = Column(SAEnum(PaymentType), nullable=False, default=PaymentType.SINGLE)
    deposit_pct = Column(Numeric(5, 2), nullable=True)
    payment_status = Column(SAEnum(PaymentStatus), nullable=False, default=PaymentStatus.UNPAID)
    delivery_destination = Column(Text, nullable=True)
    expected_lead_time = Column(String(100), nullable=True)
    order_date = Column(Date, nullable=True)
    expected_arrival_date = Column(Date, nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=False)

class SupplierPOLine(UUIDBase):
    __tablename__ = "supplier_po_lines"
    po_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_variant_id = Column(UUID(as_uuid=True), nullable=True)
    description = Column(Text, nullable=False)
    quantity = Column(Numeric(14, 4), nullable=False)
    unit_price_foreign = Column(Numeric(12, 4), nullable=False)
    line_total_foreign = Column(Numeric(14, 4), nullable=False)
